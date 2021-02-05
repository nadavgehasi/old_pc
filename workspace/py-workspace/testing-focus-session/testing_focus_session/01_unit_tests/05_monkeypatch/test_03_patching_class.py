from mock import Mock, call

from randoms import generate_random


def test_today(monkeypatch):
    mocked_random = Mock(spec=[])
    monkeypatch.setattr('randoms.Random', mocked_random)

    ###
    generate_random()
    ###

    assert mocked_random.mock_calls == [call(0, 1), call().generate()]
