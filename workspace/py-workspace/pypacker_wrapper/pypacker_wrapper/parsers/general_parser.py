from dpkt.ethernet import Ethernet as dethernet
from dpkt.ip import IP as dip
from dpkt.udp import UDP as dudp
from dpkt.tcp import TCP as dtcp
from pypacker.layer12.ethernet import Ethernet
from pypacker.layer3.ip import IP
from pypacker.layer4.tcp import TCP
from pypacker.layer4.udp import UDP

from pypacker_wrapper.parsers.example import NewProtocol, Option
from pypacker_wrapper.parsers.my_layer import MyLayer


def parse(packet: bytes):
    a = MyLayer()
    # a.
    b = Option()
    b.some_value = 2
    parsed_packet = Ethernet(packet)
    print(parsed_packet[IP].src)
    return parsed_packet


