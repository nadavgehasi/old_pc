"""
Scopes creation order
1. Session
2. Package (Experimental)
3. Module
4. Class
5. Function
"""

import pytest


@pytest.fixture(scope="session")
def scoped_session():
    print 'first'


@pytest.fixture(scope="module")
def scoped_module():
    print 'second'


@pytest.fixture
def function_scoped(tmpdir):
    # tmpdir: 3rd
    print 'fourth'


@pytest.fixture
def second_function_scoped():
    print 'fifth'


def test_nothing(function_scoped, scoped_session, scoped_module, second_function_scoped):
    assert True
