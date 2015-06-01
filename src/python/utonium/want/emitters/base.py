#!/usr/bin/env python
"""
utonium/want/emitters/base.py

The base class for objects that emitted specific shell language for want snippets.

Copyright 2015 Kevin Cureton
"""
# ---------------------------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------------------------
import logging
import string
import sys

# ---------------------------------------------------------------------------------------------
# Globals
# ---------------------------------------------------------------------------------------------
logger = logging.getLogger()

# The keywords supported by the want grammar.
ACTION_VAR_PREPEND = "var_prepend"
ACTION_VAR_APPEND = "var_append"
ACTION_VAR_SET = "var_set"
ACTION_WANT = "want"
ACTION_UNWANT = "unwant"

VALID_ACTIONS = set([
    ACTION_VAR_PREPEND,
    ACTION_VAR_APPEND,
    ACTION_VAR_SET,
    ACTION_WANT,
    ACTION_UNWANT,
])


# ---------------------------------------------------------------------------------------------
# Base class for emitters
# ---------------------------------------------------------------------------------------------
class BaseEmitter(object):

    def __init__(self, commands):
        """ Initialize an emitter object of the specified type with the command list
            that will be emitted.
        """
        if type(commands) != list:
            msg = "Invalid type for commands, must be a list"
            raise EmitterError(msg)

        self.__commands = commands


    def emit(self, unwant=False):
        """ Emit the commands in the specified shell language.

            unwant: If True, will emit commands to unwant instead of want.
        """
        for command in self.__commands:
            self._emitCommand(command)


    def _emitCommand(self, command):
        """ Emit shell language for the given command.
        """
        logger.error("The _emitCommand method must be overridden in the specific emitter.")
        raise NotImplemented
        


class EmitterError(Exception):
    pass


# ---------------------------------------------------------------------------------------------
# Module test harness
# ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(0)
