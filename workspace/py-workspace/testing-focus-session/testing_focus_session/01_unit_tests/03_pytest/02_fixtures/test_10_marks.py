"""
Will see:
-m "webview"
-m "not webview"
-m "pasten"
"""

import pytest

pytestmark = [pytest.mark.pasten, pytest.mark.pastenpasten]


@pytest.mark.webview
def test_some_view():
    pass


@pytest.mark.webview
class TestSomeViewClass(object):
    def test_some_view(self):
        pass


def test_other_thing():
    pass
