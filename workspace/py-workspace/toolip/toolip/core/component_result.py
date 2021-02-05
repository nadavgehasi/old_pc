import attr

from toolip.core.toolip_packet import ToolipPacket


@attr.s
class ComponentResult:
    """
    Define specific api for toolip component that contained data the needed for test_toolip features.
    """

    packet: ToolipPacket = attr.ib()

    @staticmethod
    def create(packet: ToolipPacket):
        return ComponentResult(packet)
