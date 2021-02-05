from dataclasses import dataclass
from typing import Iterable

from pypacker.pypacker import Packet

import itertools


class MyLayer(object):

    __hdr__ = (
        ("field", "B", 0x00),
    )

    __fields__ = ['field']

    __slots__ = ['asd']

    # def __dir__(self) -> Iterable[str]:
    #     print(super(MyLayer, self).__dir__())
    #     print(itertools.chain([self.__fields__], super(MyLayer, self).__dir__()))
    #     return itertools.chain(self.__fields__, super(MyLayer, self).__dir__())

    def _dissect(self, buf):
        pass
