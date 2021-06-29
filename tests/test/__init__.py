"""Root class for testing."""
from unittest import TestCase


class TestBase(TestCase):
    """Base class for tests."""

    def setUp(self):
        """Init tests."""
        TestCase.setUp(self)

        from source.cli import PARSER
        self.options, _args = PARSER.parse_args(args=[])
