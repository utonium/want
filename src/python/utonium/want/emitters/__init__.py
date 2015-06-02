#!/usr/bin/env python
"""
utonium/want/emitters/__init__.py

The entry-point API for want emitters.

Copyright 2015 Kevin Cureton
"""
# ---------------------------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------------------------
import logging
import string
import sys

import base
import python
import sh
import tcsh

# ---------------------------------------------------------------------------------------------
# Globals
# ---------------------------------------------------------------------------------------------
logger = logging.getLogger()

# Valid shell emitters
EMITTER_SH = "sh"
EMITTER_TCSH = "tcsh"
EMITTER_PYTHON = "python"
EMITTER_NATIVE = "native"

VALID_EMITTERS = set([
    EMITTER_SH,
    EMITTER_TCSH,
    EMITTER_PYTHON,
    EMITTER_NATIVE,
])

# ---------------------------------------------------------------------------------------------
# Factory method for instantiating emitters
# ---------------------------------------------------------------------------------------------
def spawnEmitter(emitter_type, commands, snippets):
    """ Create an emitter object of the specified type.

        emitter_type: governs what shell language is output
        commands: list of commands to emit shell language for
        snippets: list of the snippets the commands came from
    """
    if not emitter_type in VALID_EMITTERS:
        msg = "Unknown emitter type specified: %s" % emitter_type
        raise base.EmitterError(msg)

    # TODO: Make this dynamic, not a lookup via if.
#    emitter_module_name = "utnoium.want.emitters.%s" % emitter_type
#    emitter_module = __import__(emitter_module_name)
#    emitter = emitter_module.Emitter(commands)

#    emitter_module = __import__(emitter_type)
#    emitter = emitter_module.Emitter(commands)

    emitter = None
    if emitter_type == EMITTER_NATIVE:
        emitter = native.Emitter(commands, snippets)
    elif emitter_type == EMITTER_PYTHON:
        emitter = python.Emitter(commands, snippets)
    elif emitter_type == EMITTER_SH:
        emitter = sh.Emitter(commands, snippets)
    elif emitter_type == EMITTER_TCSH:
        emitter = tcsh.Emitter(commands, snippets)

    return emitter


# ---------------------------------------------------------------------------------------------
# Module test harness
# ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(0)
