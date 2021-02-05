import operator

from mock import Mock, call


def generic_fibonacci(index, op):
    if index <= 1:
        return index

    before_two, before_one = 0, 1
    for i in xrange(index - 1):
        before_two, before_one = before_one, op(before_two, before_one)
    return before_one


def test_generic_fibonacci():
    op = Mock()
    op.side_effect = operator.add

    ###
    result = generic_fibonacci(6, op)
    ###

    assert result == 8
    assert op.mock_calls == [
        call(0, 1), call(1, 1), call(1, 2), call(2, 3), call(3, 5),
    ]
