from pathlib import Path

from pytest import fixture

from pypacker_wrapper.parsers.general_parser import parse
from pypacker_wrapper.utils.cap import read_cap


@fixture
def cap():
    return read_cap(Path('/tmp/packets.cap'))


def test_regular(cap):
    for packet in cap:
        parse(packet)

    print("finished")
