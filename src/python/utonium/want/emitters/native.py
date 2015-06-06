#!/usr/bin/env python
"""
utonium/want/emitters/native.py

Emitter object for 'native'.

Copyright 2015 Kevin Cureton
"""
# ---------------------------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------------------------
import logging
import string
import sys

import base
import utonium.pathmod

# ---------------------------------------------------------------------------------------------
# Globals
# ---------------------------------------------------------------------------------------------
logger = logging.getLogger()


# ---------------------------------------------------------------------------------------------
# Code
# ---------------------------------------------------------------------------------------------
class NativeEmitter(base.BaseEmitter):
    """ The Native Emitter dumps exactly what was in want
        snippet files.
    """

    def _emitCommand(self, command):
        """ Emit shell language for the given command.
        """
        action = command['action']
        params = command['params']

        if not action in base.VALID_ACTIONS:
            msg = "Unknown emitter action: %s" % action
            raise base.EmitterError(msg)

        command = "%s %s" % (action, string.join(params, ", "))

        print(command)


# ---------------------------------------------------------------------------------------------
# Module test harness
# ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(0)
