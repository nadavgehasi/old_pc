from random import random
import os


class Random(object):
    def __init__(self, m=0, n=1):
        self.m = m
        self.n = n

    def generate(self):
        return self.m + random() * self.n


def generate_random(m=0, n=1):
    return Random(m, n).generate()


os.environ['WAIT_FOR_IT'] = 'dary'
