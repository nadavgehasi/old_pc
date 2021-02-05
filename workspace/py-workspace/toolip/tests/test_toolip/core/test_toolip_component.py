from pytest import fixture

from toolip.core.component_result import ComponentResult
from toolip.core.toolip_component import ToolipComponent
from toolip.core.toolip_packet import ToolipPacket


class DoNothingComponent(ToolipComponent):
    """
    Component that return the given packet without handling.
    """

    def handle_packet(self, packet: ToolipPacket) -> ComponentResult:
        return ComponentResult.create(packet)


@fixture
def packet() -> ToolipPacket:
    return ToolipPacket(b"010101")


@fixture
def do_nothing_component() -> DoNothingComponent:
    return DoNothingComponent()


def test_do_nothing_component(packet, do_nothing_component):
    result: ComponentResult = do_nothing_component.handle_packet(packet)
    assert result.packet == packet
