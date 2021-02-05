from nipy.core.processors import processor, state_processor
from nipy.queues.redis_queues import read, write


@processor("FILE-LOGGER-INPUT", "FILE-LOGGER-OUTPUT", read, write)
def print_logger(unit):
    print(unit)


@state_processor("FILE-LOGGER-OUTPUT", "COUNTER-OUTPUT", read, write)
def count_amount(unit, state):
    state["amount"] += len(unit)
    return unit, state

class CountProcessor(Processor):
    def __init__(self, asd):
        self.asd= asd
