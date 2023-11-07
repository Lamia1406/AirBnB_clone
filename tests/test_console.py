#!/usr/bin/python3
"""defines unittests for console.py.

Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    """

import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_prompting(unittest.TestCase):
    """Unittests for testing prompt of the HBNB entry command
    interpreter.
    """

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestHBNBCommand_help(unitteste.TestCase):
    """unittests for testing help messages fot the HBNB command
    interpreter.
    """

    def test_help_quit(self):
        h = "Quit command to exit the program."
        with patch("sys.stdout". new=StringIO as output:
                self.assertFalse(HBNBCommand().onecmd("help quit"))
                self.assertEqual(h, output.getvalue().strip())
