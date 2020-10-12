#!/usr/bin/python3
"""Unittest Console Module"""

from console import HBNBCommand
import unittest


class Test_Console(unittest.TestCase):

    def test_quit(self):
        """Test quit command"""
        self.assertIsNot(HBNBCommand.do_quit, True)

    def test_EOF(self):
        """Test quit command"""
        self.assertIsNot(HBNBCommand.do_EOF, True)


if __name__ == "__main__":
    unittest.main()
