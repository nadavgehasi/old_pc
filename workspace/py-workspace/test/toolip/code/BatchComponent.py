from code.Component import Component


class BatchComponent(Component):
    def __init__(self):
        super().__init__()

    def run(self, **kwargs):
        pass

    def handle_batch(self, batch, *batch_handlers):
        for arg in batch_handlers:
            arg.handle_batch(batch)

    def handle_packet(self, packet, *args):
        raise NotImplementedError

