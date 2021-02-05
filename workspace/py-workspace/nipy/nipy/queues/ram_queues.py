from queue import Queue
from nipy.utils import get_random_queue

QUEUES = {"random": get_random_queue()}


def read(queue_name):
    if queue_name in QUEUES.keys():
        return QUEUES[queue_name].get()
    return None


def write(queue_name, data):
    if queue_name not in QUEUES:
        QUEUES[queue_name] = Queue()
    QUEUES[queue_name].put(data)



