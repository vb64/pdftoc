# coding: utf-8
"""Console client stuff.

make test T=test_console.py
"""
import os

from . import TestBase


class TestConsole(TestBase):
    """Tests console client."""

    def test_noargs(self):
        """Call without args."""
        from source.cli import main

        assert main([], self.options) == 1

    def test_args(self):
        """Call with arg."""
        from source.cli import main

        assert main([os.path.join('source', 'toc.json')], self.options) == 0

    def _test_nodirs(self):
        """Target without dirs."""
        from source.cli import main

        assert main([os.path.join('fixtures', 'nodir.json')], self.options) == 0
