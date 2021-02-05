from queue import Queue
from random import randint


def get_random_unit():
    return {
        "id": randint(0, 10000),
        "content": str(randint(0, 10000)),
        }


def get_random_queue():
    queue = Queue()
    for _ in range(10):
        queue.put(get_random_unit())
    return queue