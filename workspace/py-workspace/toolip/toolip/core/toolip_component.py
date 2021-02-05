import abc

from toolip.core.component_result import ComponentResult
from toolip.core.toolip_packet import ToolipPacket


class ToolipComponent(metaclass=abc.ABCMeta):
    """
    Interface for ToolipComponents
    """

    @abc.abstractmethod
    def handle_packet(self, packet: ToolipPacket) -> ComponentResult:
        pass
