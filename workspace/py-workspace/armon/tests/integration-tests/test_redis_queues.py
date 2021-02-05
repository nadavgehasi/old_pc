from armon.utils.queues.redis_queues import RedisReader, RedisWriter


def test_read_and_write():
    with RedisReader(queue_name="asd") as r, RedisWriter(queue_name="asd") as w:
        unit = "blabla"
        w.write(unit)
        print(r.read())
