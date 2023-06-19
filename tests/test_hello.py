"""Testing hello module."""
from python_poetry_package.hello import hello


def test_hello():
    """Tests if hello() working correctly"""
    assert hello() == "Hello, World!"
