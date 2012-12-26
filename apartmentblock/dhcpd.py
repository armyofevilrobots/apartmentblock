import socket
import logging
import select
from dpkt import dhcp
from dpkt import udp
from dpkt import ip
from dpkt import ethernet

BOOTP_PORT_REQUEST = 67
BOOTP_PORT_REPLY = 68
DHCP_PKT_LEN = 556


class DHCPD:
    """DHCP server."""
    def __init__(self):
        self.bind()

    def bind(self):
        """Binds the socket."""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,
                             socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("0.0.0.0", 67))
        self.sock = sock

    def handle(self, packet, srcip, srcport):
        """Respond to a dhcp pkt."""
        #print dir(packet)
        print dir(packet)
        print "OP", packet.op
        print "xis", packet.xid
        print ["%02x" % ord(x) for x in packet.chaddr]
        print packet.ciaddr
        print "from", srcip,":",srcport

    def listen(self):
        while True:
            try:
                readable, writable, exclist = \
                        select.select(
                                [self.sock, ],
                                [],
                                [self.sock, ])
                for dhcp_sock in readable:
                    data, (addr, port) = dhcp_sock.recvfrom(DHCP_PKT_LEN)
                    #packet = udp.UDP(data)
                    dhcp_pkt = dhcp.DHCP(data)
                    self.handle(dhcp_pkt, addr, port)
            except Exception, e:
                logging.error("Failure: %s", str(e))
