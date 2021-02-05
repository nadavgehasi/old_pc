import redis
import attr
from .reader import Reader
from .writer import Writer


@attr.s
class RedisBase:
    queue_name = attr.ib()
    host = attr.ib(default="redis")
    port = attr.ib(default=6379)
    connection = attr.ib(init=False, default=None)

    def __enter__(self):
        self.connection = redis.Redis(host=self.host, port=self.port)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


@attr.s
class RedisReader(Reader, RedisBase):
    def read(self):
        return self.connection.blpop(self.queue_name)[1].decode()


@attr.s
class RedisWriter(Writer, RedisBase):
    def write(self, unit):
        if unit is not None:
            self.connection.rpush(self.queue_name, unit)
        self.connection.close()
