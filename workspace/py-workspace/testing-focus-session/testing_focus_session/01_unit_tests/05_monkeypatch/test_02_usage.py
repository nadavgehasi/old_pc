from mock import Mock

from randoms import Random

import os


def test_generate_random_a(monkeypatch):
    monkeypatch.setattr(Random, 'today', Mock())


def test_generate_random_b(monkeypatch):
    monkeypatch.setattr('randoms.Random.generate', Mock())


def test_generate_random_d(monkeypatch):
    monkeypatch.setenv('WAIT_FOR_IT', 'legen', prepend=':')
    assert os.environ['WAIT_FOR_IT'] == 'legen:dary'
