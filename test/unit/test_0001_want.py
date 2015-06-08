#!/usr/bin/env python
"""
unit/test_0001_want.py

Copyright (c) 2015 Kevin Cureton
"""
# ---------------------------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------------------------
import logging
import os
import nose.tools
import re
import string
import sys

import helper

import utonium.want

# ---------------------------------------------------------------------------------------------
# Globals
# ---------------------------------------------------------------------------------------------
logger = logging.getLogger()

TEST_NAME = "test_0001_want"

# ---------------------------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------------------------
def setup():
    print("%s setup..." % TEST_NAME)

    os.environ['UTONIUM_WANT_PATH'] = os.path.join(helper.WANT_ROOT, "snippets")


def teardown():
    print("%s teardown..." % TEST_NAME)


def test_listSnippets():
    """ Want a bunch of the test snippets.
    """
    print("Executing test_listSnippets...")

    all_snippets = utonium.want.listSnippets()
    expected_snippets = [ re.sub(r'\.want$', '', x) for x in sorted(os.listdir(os.environ['UTONIUM_WANT_PATH'])) ]
    nose.tools.assert_equal(all_snippets, expected_snippets)


def test_wantSnippet():
    """ Test the wantSnippet API method.
    """
    print("Executing test_wantSnippet...")

    starting_path = os.environ['PATH']

    utonium.want.wantSnippet("python-2.7.8", emitter_type="python")
    expected_result = "/opt/python/2.7.8/bin" + os.pathsep + starting_path
    nose.tools.assert_equal(expected_result, os.environ['PATH'])

    utonium.want.wantSnippet("ffmpeg-1.1.4", emitter_type="python")
    expected_result = expected_result + os.pathsep + "/opt/ffmpeg/1.1.4/bin"
    nose.tools.assert_equal(expected_result, os.environ['PATH'])


#var_prepend PATH /opt/python/2.7.8/bin
#var_prepend PYTHONPATH /opt/python/2.7.8/lib

    # Test with the FFMPEG snippet.
#    utonium.want.wantSnippet("ffmpeg-1.1.4", emitter_type="sh")

#    nose.tools.assert_not_equal()

#    utonium.want.unwantSnippet(snippet, emitter_type="python")
#    utonium.want.whichSnippet(snippet)
#    utonium.want.whereSnippet(snippet)
#    utonium.want.wantedSnippets()
#    utonium.want.parseSnippet(snippet)


#    os.environ[helper.ENV_VAR] = helper.TEST_PATH
#    utonium.pathmod.modifyPathsForEnvVar(utonium.pathmod.ACTION_APPEND, helper.ENV_VAR, helper.APPEND_PATH)
#    nose.tools.assert_not_equal(os.environ[helper.ENV_VAR], helper.APPEND_PATH_RESULT)


# ---------------------------------------------------------------------------------------------
# Execute main and exit with the returned status.
# ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(0)
