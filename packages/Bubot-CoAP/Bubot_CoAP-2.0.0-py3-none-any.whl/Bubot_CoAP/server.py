import asyncio
import logging
import random
from socket import AF_INET, AF_INET6

from aio_dtls.connection_manager.connection_manager import ConnectionManager

from bubot_helpers.ExtException import ExtException
from . import defines
from .layers.block_layer import BlockLayer
from .layers.callback_layer import CallbackLayer
from .layers.endpoint_layer import EndpointLayer
from .layers.message_layer import MessageLayer
from .layers.observe_layer import ObserveLayer
from .layers.request_layer import RequestLayer
from .layers.resource_layer import ResourceLayer
from .messages.message import Message
from .messages.request import Request
from .resources.resource import Resource
from .utils import Tree, Timer

__author__ = 'Giacomo Tanganelli'
logger = logging.getLogger('Bubot_CoAP')


class Server:
    """
    Implementation of the CoAP server
    """

    def __init__(self, *, starting_mid=None, cb_ignore_listen_exception=None, client_manager=None, **kwargs):
        """
        Initialize the server.

        :param starting_mid: used for testing purposes
        :param cb_ignore_listen_exception: Callback function to handle exception raised during the socket listen operation
        """
        self.max_retransmit = kwargs.get('max_retransmit', defines.MAX_RETRANSMIT)
        self.ask_timeout = kwargs.get('ask_timeout', defines.ACK_TIMEOUT)
        self.exchange_lifetime = kwargs.get('exchange_lifetime', defines.EXCHANGE_LIFETIME)
        self.loop = kwargs.get('loop', asyncio.get_event_loop())

        self.stopped = asyncio.Event()
        self.stopped.clear()
        self.multicast_address = {
            AF_INET: kwargs.get('multicast_ipv4', [defines.ALL_COAP_NODES]),
            AF_INET6: kwargs.get('multicast_ipv6', [defines.ALL_COAP_NODES_IPV6])
        }
        self.multicast_port = kwargs.get('multicast_port', defines.COAP_DEFAULT_PORT)
        self.to_be_stopped = []
        self.loop.create_task(self.purge())
        self.endpoint_layer = EndpointLayer(self)
        self.message_layer = MessageLayer(self, starting_mid)
        self.block_layer = BlockLayer()
        self.observe_layer = ObserveLayer()
        self.request_layer = RequestLayer(self)
        self.resource_layer = ResourceLayer(self)
        self.callback_layer = CallbackLayer(self)
        self.dtls_connection_manager = ConnectionManager(secret='test')
        # Resource directory
        root = Resource('root', self, visible=False, observable=False, allow_children=False)
        root.path = '/'
        self.client_manager = client_manager
        self.root = Tree()
        self.root["/"] = root
        self._serializer = None
        self._cb_ignore_listen_exception = cb_ignore_listen_exception

    async def purge(self):
        """
        Clean old and complete transactions

        """
        while not self.stopped.is_set():
            try:
                await asyncio.wait_for(self.stopped.wait(), 15)  # defines.EXCHANGE_LIFETIME)
            except asyncio.TimeoutError:
                pass
            self.message_layer.purge()

    async def close(self):
        """
        Stop the server.

        """
        try:
            logger.info("Stop server")
            self.stopped.set()
            for event in self.to_be_stopped:
                event.set()
            await asyncio.sleep(0.001)
            self.endpoint_layer.close()
        except Exception as err:
            raise ExtException(parent=err, action='coap server closing')

    async def receive_request(self, transaction):
        """
        Handle requests coming from the udp socket.

        :param transaction: the transaction created to manage the request
        """

        async with transaction.lock:

            transaction.separate_timer = await self._start_separate_timer(transaction)

            self.block_layer.receive_request(transaction)

            if transaction.block_transfer:
                await self._stop_separate_timer(transaction.separate_timer)
                self.message_layer.send_response(transaction)
                await self.send_datagram(transaction.response)
                return

            await self.observe_layer.receive_request(transaction)
            if transaction.resource is None:
                await self.request_layer.receive_request(transaction)

            if transaction.resource is not None and transaction.resource.changed:
                await self.notify(transaction.resource)
                transaction.resource.changed = False
            elif transaction.resource is not None and transaction.resource.deleted:
                await self.notify(transaction.resource)
                transaction.resource.deleted = False

            self.observe_layer.send_response(transaction)

            self.block_layer.send_response(transaction)

            await self._stop_separate_timer(transaction.separate_timer)

            self.message_layer.send_response(transaction)

            if transaction.response is not None:
                if transaction.response.type == defines.Types["CON"]:
                    await self.start_retransmission(transaction, transaction.response)
                if transaction.request.multicast:
                    await asyncio.sleep(random.uniform(0, 10))
                    transaction.response.source = (transaction.response.source[0], None)
                await self.send_datagram(transaction.response)
        await asyncio.sleep(0)

    async def send_message(self, message, no_response=False, endpoint=None, **kwargs):
        try:
            if isinstance(message, Request):
                if message.token is None:
                    message.token = self.message_layer.fetch_token()

                request = self.request_layer.send_request(message)
                request = self.observe_layer.send_request(request)
                request = self.block_layer.send_request(request)
                if no_response:
                    # don't add the send message to the message layer transactions
                    await self.send_datagram(request, **kwargs)
                    logger.debug(f'Send no response request {request}')
                    return
                transaction = self.message_layer.send_request(request)
                await self.send_datagram(transaction.request, endpoint=endpoint, **kwargs)
                logger.info("Send request     - " + str(request))

                if transaction.request.type == defines.Types["CON"]:
                    await self.start_retransmission(transaction, transaction.request)
                response = await self.callback_layer.wait(request, **kwargs)
                return response

            elif isinstance(message, Message):
                message = self.observe_layer.send_empty(message)
                message = self.message_layer.send_empty(None, None, message)
                await self.send_datagram(message, endpoint=endpoint, **kwargs)
        except (asyncio.TimeoutError, asyncio.CancelledError) as err:
            raise err
        except Exception as err:
            raise ExtException(parent=err)

    async def send_datagram(self, message, *, endpoint=None, **kwargs):
        """
        Send a message through the udp socket.

        :type message: Message
        :param message: the message to send
        """
        try:
            # if not self.stopped.isSet():
            # host, port = message.destination
            # host, port = message.source
            if endpoint is None:
                endpoint = self.endpoint_layer.find_sending_endpoint(message)

            if not endpoint:
                raise KeyError(
                    f'Not found endpoint for {message.source}')  # todo исключения не обрабатываются при отправке из resonse

            async with endpoint.lock:
                await endpoint.send_message(message, **kwargs)
        except Exception as err:
            raise err

    def add_resource(self, path, resource):
        """
        Helper function to add resources to the resource directory during server initialization.

        :param path: the path for the new created resource
        :type resource: Resource
        :param resource: the resource to be added
        """

        assert isinstance(resource, Resource)
        path = path.strip("/")
        paths = path.split("/")
        actual_path = ""
        i = 0
        for p in paths:
            i += 1
            actual_path += "/" + p
            try:
                res = self.root[actual_path]
            except KeyError:
                res = None
            if res is None:
                resource.path = actual_path
                self.root[actual_path] = resource
        return True

    def remove_resource(self, path):
        """
        Helper function to remove resources.

        :param path: the path for the unwanted resource
        :rtype : the removed object
        """

        path = path.strip("/")
        paths = path.split("/")
        actual_path = ""
        i = 0
        for p in paths:
            i += 1
            actual_path += "/" + p
        try:
            res = self.root[actual_path]
        except KeyError:
            res = None
        if res is not None:
            del (self.root[actual_path])
        return res

    async def start_client(self, url, **kwargs):
        return await self.endpoint_layer.start_client(url, **kwargs)

    async def add_endpoint(self, url: str, **kwargs):
        """
        Helper function to add endpoint to the endpoint directory during server initialization.

        :param endpoint: the endpoint to be added

        """
        return await self.endpoint_layer.add_by_netloc(url, **kwargs)

    #
    # def remove_endpoint(self, **kwargs):
    #     return self.endpoint_layer.remove(**kwargs)
    #     pass

    @staticmethod
    async def wait_for_retransmit_thread(transaction):
        """
        Only one retransmit thread at a time, wait for other to finish

        """
        if hasattr(transaction, 'retransmit_thread'):
            while transaction.retransmit_thread is not None:
                logger.debug("Waiting for retransmit thread to finish ...")
                await asyncio.sleep(0.01)
                continue

    async def send_block_request(self, transaction):
        """
        A former request resulted in a block wise transfer. With this method, the block wise transfer
        will be continued, including triggering of the retry mechanism.

        :param transaction: The former transaction including the request which should be continued.
        """
        transaction = self.message_layer.send_request(transaction.request)
        # ... but don't forget to reset the acknowledge flag
        transaction.request.acknowledged = False
        try:
            await self.send_datagram(transaction.request)
        except Exception as err:
            logger.error(err)
            transaction.completed = True
        if transaction.request.type == defines.Types["CON"]:
            await self.start_retransmission(transaction, transaction.request)

    async def start_retransmission(self, transaction, message):
        """
        Start the retransmission task.

        :type transaction: Transaction
        :param transaction: the transaction that owns the message that needs retransmission
        :type message: Message
        :param message: the message that needs the retransmission task
        """
        # async with transaction.lock:
        if message.type == defines.Types['CON'] and message.acknowledged and not transaction.over_tcp:
            future_time = random.uniform(defines.ACK_TIMEOUT, (defines.ACK_TIMEOUT * defines.ACK_RANDOM_FACTOR))
            transaction.retransmit_thread = self.loop.create_task(
                self._retransmit(transaction, message, future_time, 0))
            transaction.retransmit_stop = asyncio.Event()
            self.to_be_stopped.append(transaction.retransmit_stop)
            await asyncio.sleep(0.001)

    async def _retransmit(self, transaction, message, future_time, retransmit_count):
        """
        Thread function to retransmit the message in the future

        :param transaction: the transaction that owns the message that needs retransmission
        :param message: the message that needs the retransmission task
        :param future_time: the amount of time to wait before a new attempt
        :param retransmit_count: the number of retransmissions
        """
        async with transaction.lock:
            logger.debug("retransmit loop ... enter")
            while retransmit_count < defines.MAX_RETRANSMIT and (not message.acknowledged and not message.rejected) \
                    and not self.stopped.is_set():
                if transaction.retransmit_stop is not None:
                    try:
                        await asyncio.wait_for(transaction.retransmit_stop.wait(), future_time)
                    except asyncio.TimeoutError:
                        pass
                if not message.acknowledged and not message.rejected and not self.stopped.is_set():
                    retransmit_count += 1
                    future_time *= 2
                    if retransmit_count < defines.MAX_RETRANSMIT:
                        logger.debug("retransmit loop ... retransmit Request")
                        await self.send_datagram(message)

            if message.acknowledged or message.rejected:
                message.timeouted = False
            else:
                logger.warning("Give up on message {message}".format(message=message.line_print))
                message.timeouted = True
                if message.observe is not None:
                    self.observe_layer.remove_subscriber(message)

                # Inform the user, that nothing was received
                # self._callback(None)
                a = 1

            try:
                self.to_be_stopped.remove(transaction.retransmit_stop)
            except ValueError:
                pass
            transaction.retransmit_stop = None
            transaction.retransmit_thread = None
            logger.debug("retransmit loop ... exit")

    async def _start_separate_timer(self, transaction):
        """
        Start a thread to handle separate mode.

        :type transaction: Transaction
        :param transaction: the transaction that is in processing
        :rtype : the Timer object
        """
        t = Timer(defines.ACK_TIMEOUT, self.send_ack, (transaction,))
        await asyncio.sleep(0.001)
        return t

    @staticmethod
    async def _stop_separate_timer(timer):
        """
        Stop the separate Thread if an answer has been already provided to the client.

        :param timer: The Timer object
        """
        await timer.cancel()

    async def send_ack(self, transaction, message=None):
        """
        Sends an ACK message for the request.

        :param transaction: the transaction that owns the request
        """
        if message is None:
            message = transaction.request
        ack = Message()
        ack.type = defines.Types['ACK']
        async with transaction.lock:
            if not message.acknowledged and message.type == defines.Types["CON"]:
                ack = self.message_layer.send_empty(transaction, message, ack)
                if ack.type is not None and ack.mid is not None:
                    await self.send_datagram(ack)

    async def notify(self, resource):
        """
        Notifies the observers of a certain resource.

        :param resource: the resource
        """
        observers = self.observe_layer.notify(resource)
        logger.debug("Notify")
        for transaction in observers:
            with transaction:
                transaction.response = None
                transaction = self.request_layer.receive_request(transaction)
                transaction = self.observe_layer.send_response(transaction)
                transaction = self.block_layer.send_response(transaction)
                transaction = self.message_layer.send_response(transaction)
                if transaction.response is not None:
                    if transaction.response.type == defines.Types["CON"]:
                        await self.start_retransmission(transaction, transaction.response)

                    await self.send_datagram(transaction.response)
