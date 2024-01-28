import logging
import socket
import ssl

from aio_dtls import DtlsSocket

from .udp import UdpCoapEndpoint
from ..coap_udp_protocol import CoapDatagramProtocol

logger = logging.getLogger(__name__)


class UdpCoapsEndpoint(UdpCoapEndpoint):
    scheme = 'coaps'
    ssl_transport = 1  # MBEDTLS_SSL_TRANSPORT_DATAGRAM = DTLS

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.cert_filename = kwargs['certfile']
            self.key_filename = kwargs['keyfile']
        except KeyError as err:
            raise KeyError(f'{err} in CoapEndpoint not defined')

    def init_unicast_ip4_by_address(self, address, **kwargs):
        self._multicast = None
        self._address = address
        self._family = socket.AF_INET
        _sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        _sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._sock = DtlsSocket(
            sock=_sock,
            endpoint=self,
            **self.params.get('socket_props', {})
        )
        self._sock.bind(address)

    def init_unicast_ip6_by_address(self, address, **kwargs):
        self._multicast = None
        self._address = address
        self._family = socket.AF_INET6
        _sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        _sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._sock = DtlsSocket(
            sock=_sock,
            endpoint=self,
            **self.params.get('socket_props', {})
        )
        # self._sock = ssl.wrap_socket(
        #     _sock,
        #     # keyfile=self.key_filename, certfile=self.cert_filename,
        #     server_side=True,
        #     **self.params.get('socket_props', {})
        # )
        self._sock.bind(address)

    def send(self, data, address, **kwargs):
        self._sock.sendto(data, address, **kwargs)

    async def listen(self, server):
        await self._sock.listen(server, CoapDatagramProtocol)
        if not self.address[1]:
            self._address = self.sock.address
        logger.debug(f'run {"multicast " if self._multicast else ""}'
                     f'endpoint {self._sock.address[0]}:{self._sock.address[1]}')

    def raw_sendto(self, data, address):
        self._sock.raw_sendto(data, address)

    # async def send_alert(self, data, address, **kwargs):
    #     self._sock.send_alert(data, address, **kwargs)

    def close(self):
        if self._sock:
            self._sock.close()
