#!/usr/bin/env python
"""
utonium/want/emitters/tcsh.py

Emitter object for 'tcsh'.

Copyright 2015 Kevin Cureton
"""
# ---------------------------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------------------------
import logging
import string
import sys

import base

# ---------------------------------------------------------------------------------------------
# Globals
# ---------------------------------------------------------------------------------------------
logger = logging.getLogger()


# ---------------------------------------------------------------------------------------------
# Code
# ---------------------------------------------------------------------------------------------
class TcshEmitter(base.BaseEmitter):
    """ The Tcsh Emitter emits csh/tcsh shell language.
    """

    def _emitCommand(self, command):
        """ Emit shell language for the given command.
        """
        action = command['action']
        params = command['params']

        the_command = None
        if action == base.ACTION_VAR_PREPEND:
            env_var_name = params[0]
            path = params[1]
            the_command = "setenv %s `pathmod --prepend %s %s`" % (env_var_name, env_var_name, path)

        elif action == base.ACTION_VAR_APPEND:
            env_var_name = params[0]
            path = params[1]
            the_command = "setenv %s `pathmod --append %s %s`" % (env_var_name, env_var_name, path)

        elif action == base.ACTION_VAR_SET:
            env_var_name = params[0]
            env_var_value = params[1]
            the_command = "setenv %s %s" % (env_var_name, env_var_value)

        else:
            msg = "Unknown emitter action: %s" % action
            raise base.EmitterError(msg)

        print(the_command)


# ---------------------------------------------------------------------------------------------
# Module test harness
# ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(0)
