"""Console client stuff.

make test T=test_console.py
"""
from . import TestBase


class TestConsole(TestBase):
    """Tests console client."""

    def test_default(self):
        """Call without args."""
        from source import main

        assert main() == 0
