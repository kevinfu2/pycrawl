import pytest

from pycrawl.main import main

@pytest.fixture()
def function():
    return "func"

class TestMain(object):

    def test_smoke(self):
        assert main([]) == 0