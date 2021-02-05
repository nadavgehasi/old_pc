from pathlib import Path
from typing import List

from dpkt.pcap import Reader, Writer


def read_cap(path: Path = Path('/tmp/packets.cap')) -> List[bytes]:
    cap = Reader(path.open('rb'))
    packets = [packet for timestamp, packet in list(cap)]
    return packets


def write_cap(packets: List[bytes], path: Path):
    cap = Writer(path.open('wb'))
    for packet in packets:
        cap.writepkt(packet)
    cap.close()

