#!/usr/bin/env python
"""
utonium/want/emitters/sh.py

Emitter object for 'sh/bash'.

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

# ---------------------------------------------------------------------------------------------
# Globals
# ---------------------------------------------------------------------------------------------
logger = logging.getLogger()


# ---------------------------------------------------------------------------------------------
# Code
# ---------------------------------------------------------------------------------------------
class ShEmitter(base.BaseEmitter):
    """ The Sh Emitter emits sh/bash shell language.
    """

    def _emitCommand(self, command, unwant=False):
        """ Emit shell language for the given command.
        """
        action = command['action']
        params = command['params']

        the_command = None
        if action == base.ACTION_VAR_PREPEND:
            env_var_name = params[0]
            path = params[1]
            if unwant:
                the_command = "export %s=`pathmod --delete %s %s`" % (env_var_name, env_var_name, path)
            else:
                the_command = "export %s=`pathmod --prepend %s %s`" % (env_var_name, env_var_name, path)

        elif action == base.ACTION_VAR_APPEND:
            env_var_name = params[0]
            path = params[1]
            if unwant:
                the_command = "export %s=`pathmod --delete %s %s`" % (env_var_name, env_var_name, path)
            else:
                the_command = "export %s=`pathmod --append %s %s`" % (env_var_name, env_var_name, path)

        elif action == base.ACTION_VAR_SET:
            env_var_name = params[0]
            env_var_value = params[1]
            if unwant:
                the_command = "unset %s" % (env_var_name)
            else:
                the_command = "export %s=%s" % (env_var_name, env_var_value)

        else:
            msg = "Unknown emitter action: %s" % action
            raise base.EmitterError(msg)

        print(the_command)


# ---------------------------------------------------------------------------------------------
# Module test harness
# ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(0)
