import redis


def read(queue_name):
    r = redis.Redis(host="127.0.0.1", port=6379)
    result = r.blpop(queue_name)[1].decode()
    r.close()
    return result


def write(queue_name, value):
    # TODO what if the value is None?
    if value is not None:
        r = redis.Redis(host="127.0.0.1", port=6379)
        r.rpush(queue_name, value)
        r.close()
