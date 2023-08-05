import os
import sys


class Config(object):
    """Configuration for this test suite

    This creates a variable named CONFIG (${CONFIG} when included
    in a test as a variable file. It also configures PYTHONPATH
    so that the tests can find the libraries being tested.

    Example:

    *** Settings ***
    | Variable | ../resources/config.py

    *** Test Cases ***
    | Example
    | | log | username: ${CONFIG.username}
    | | log | root url: ${CONFIG.root_url}

    """

    def __init__(self):
        _root = os.getcwd()
        sys.path.append(_root)

        self.python = sys.executable

    def __str__(self):
        return "<Config: %s>" % str(self.__dict__)

# This creates a variable that robot can see named ${CONFIG}
CONFIG = Config()
