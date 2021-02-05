class Component:
    def __init__(self, ):
        print("Init")

    def run(self, packet):
        return self.handle_packet(packet)

    def handle_packet(self, packet):
        pass
