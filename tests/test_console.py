#!/usr/bin/python3
"""Unit tests for console.py"""

import unittest
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Tests for HBNBCommand class"""

    def test_quit(self):
        self.assertTrue(HBNBCommand().do_quit(""))

    def test_EOF(self):
        self.assertTrue(HBNBCommand().do_EOF(""))


if __name__ == "__main__":
    unittest.main()

