import sys

import pytest


@pytest.mark.xfail(reason="blah")
def test_f1():  # XFAIL with reason
    assert False


@pytest.mark.xfail(run=False)
def test_f2():  # XFAIL but not really run test
    assert False


@pytest.mark.xfail("sys.version_info.major == 2")
def test_f3():  # XFAIL only on python 2
    assert False


@pytest.mark.xfail(raises=Exception)
def test_f4():  # XFAIL only with specific exception
    raise Exception()


@pytest.mark.xfail()
def test_f5():  # XPASS (unexpectedly passed) but ignored
    assert True


@pytest.mark.xfail(strict=True)
def test_f6():  # Test will fail and not ignored
    assert True


def test_f7():  # XFAIL only from specific test flow
    if sys.version_info.major < 3:
        pytest.xfail("reason")
