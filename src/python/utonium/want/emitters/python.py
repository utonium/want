#!/usr/bin/env python
"""
utonium/want/emitters/python.py

Emitter object for 'python'.

Copyright 2015 Kevin Cureton
"""
# ---------------------------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------------------------
import logging
import os
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
class PythonEmitter(base.BaseEmitter):
    """ The Python Emitter does the work prescribed by the command's
        action instead of emitting shell language. So internal to
        Python, the want API behaves like regular methods.
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
            print("NAME: %s, PATH: %s" % (env_var_name, path))
            os.environ[env_var_name] = utonium.pathmod.prependPathToEnvVar(env_var_name, path, as_str=True)

        elif action == base.ACTION_VAR_APPEND:
            env_var_name = params[0]
            path = params[1]
            os.environ[env_var_name] = utonium.pathmod.appendPathToEnvVar(env_var_name, path, as_str=True)

        elif action == base.ACTION_VAR_SET:
            env_var_name = params[0]
            env_var_value = params[1]
            os.environ[env_var_name] = env_var_value

        else:
            msg = "Unknown emitter action: %s" % action
            raise base.EmitterError(msg)


# ---------------------------------------------------------------------------------------------
# Module test harness
# ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(0)
