import attr


@attr.s
class ToolipPacket:
    """
    The base packet used in toolip components
    """

    data: bytes = attr.ib()
