"""Console client stuff.

make test T=test_console.py
"""
from . import TestBase


class TestConsole(TestBase):
    """Tests console client."""

    @staticmethod
    def test_default():
        """Call without args."""
        from source.cli import main

        assert main() == 0
