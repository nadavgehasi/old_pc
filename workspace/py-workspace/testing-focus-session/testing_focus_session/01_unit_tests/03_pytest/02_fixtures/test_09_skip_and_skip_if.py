

@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():
    pass


def test_1():
    if True:
        pytest.skip("unsupported configuration")


@pytest.mark.skipif(
    "sys.version_info < (3,8)", reason="requires python3.8 or higher"
)
def test_2(): pass


@pytest.mark.skipif('os.environ.get("TEST_LEVEL") != "unit"')
def test_3(): pass
