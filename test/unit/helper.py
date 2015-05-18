#!/usr/bin/env python
# ---------------------------------------------------------------------------------------------
"""
unit/helper.py

Things used by all the tests.

Copyright (c) 2015 Kevin Cureton
"""
# ---------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------------------------
import os
import string
import sys


# ---------------------------------------------------------------------------------------------
# Globals
# ---------------------------------------------------------------------------------------------
ENV_VAR = "TEST_PATH"
TEST_PATH = "/Users/kcureton/Projects/devops/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/kixeye/bin"

APPEND_PATH = "/opt/utonium/want/bin"
APPEND_PATH_RESULT = TEST_PATH + os.path.pathsep + APPEND_PATH

PREPEND_PATH = "/opt/utonium/want/bin"
PREPEND_PATH_RESULT = TEST_PATH + os.path.pathsep + PREPEND_PATH

DELETE_PATH = "/usr/local/bin"
DELETE_PATH_RESULT = "/Users/kcureton/Projects/devops/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/kixeye/bin"


# ---------------------------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
# Execute main and exit with the returned status.
# ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(0)
