from mock import Mock, call

from randoms import generate_random


def test_generate_random__wrong_way(monkeypatch):
    mocked_random = Mock(spec=[], return_value=4)
    monkeypatch.setattr('random.random', mocked_random)

    ###
    generate_random()
    ###

    assert mocked_random.mock_calls == [call()]


def test_generate_random__correct_way(monkeypatch):
    mocked_random = Mock(spec=[], return_value=4)
    monkeypatch.setattr('randoms.random', mocked_random)

    ###
    generate_random()
    ###

    assert mocked_random.mock_calls == [call()]
