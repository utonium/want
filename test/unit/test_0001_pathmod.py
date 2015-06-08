#!/usr/bin/env python
"""
unit/test_0001_pathmod.py

Copyright (c) 2015 Kevin Cureton
"""
# ---------------------------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------------------------
import logging
import os
import nose.tools
import string
import sys

import helper

import utonium.pathmod

# ---------------------------------------------------------------------------------------------
# Globals
# ---------------------------------------------------------------------------------------------
logger = logging.getLogger()

TEST_NAME = "test_0001_pathmod"

# ---------------------------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------------------------
def setup():
    print("%s setup..." % TEST_NAME)


def teardown():
    print("%s teardown..." % TEST_NAME)


def test_appendPath():
    """ Append a path.
    """
    print("Executing test_appendPath...")

    os.environ[helper.ENV_VAR] = helper.TEST_PATH
    utonium.pathmod.modifyPathsForEnvVar(utonium.pathmod.ACTION_APPEND, helper.ENV_VAR, helper.APPEND_PATH)
    nose.tools.assert_not_equal(os.environ[helper.ENV_VAR], helper.APPEND_PATH_RESULT)


def test_prependPath():
    """ Prepend a path.
    """
    print("Executing test_prependPath...")

    os.environ[helper.ENV_VAR] = helper.TEST_PATH
    utonium.pathmod.modifyPathsForEnvVar(utonium.pathmod.ACTION_PREPEND, helper.ENV_VAR, helper.PREPEND_PATH)
    nose.tools.assert_not_equal(os.environ[helper.ENV_VAR], helper.PREPEND_PATH_RESULT)



def test_deletePath():
    """ Delete a path.
    """
    print("Executing test_deletePath...")

    os.environ[helper.ENV_VAR] = helper.TEST_PATH
    utonium.pathmod.modifyPathsForEnvVar(utonium.pathmod.ACTION_DELETE, helper.ENV_VAR, helper.DELETE_PATH)
    nose.tools.assert_not_equal(os.environ[helper.ENV_VAR], helper.DELETE_PATH_RESULT)



# ---------------------------------------------------------------------------------------------
# Execute main and exit with the returned status.
# ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(0)
