from mock import Mock, call

from randoms import generate_random


def test_generate_random(monkeypatch):
    mocked_generate = Mock(spec=[])
    monkeypatch.setattr('randoms.Random.generate', mocked_generate)

    ###
    generate_random()
    ###

    assert mocked_generate.mock_calls == [call()]
