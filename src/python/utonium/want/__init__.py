#!/usr/bin/env python
"""
utonium/want/__init__.py

Primary Python API for the want system.

Copyright 2015 Kevin Cureton
"""
# ---------------------------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------------------------
import logging
import os
import re
import string
import sys

import utonium.pathmod
import emitters
import emitters.base


# ---------------------------------------------------------------------------------------------
# Globals
# ---------------------------------------------------------------------------------------------
logger = logging.getLogger()

# The extension for snippet files.
WANT_SNIPPET_EXTENSION = ".want"


# ---------------------------------------------------------------------------------------------
# Public code
# ---------------------------------------------------------------------------------------------
def listSnippets():
    """ List all the snippets found in the search paths.
    """
    logger.debug("Called listSnippets...")

    paths = __getWantPaths()

    snippets = list()
    for path in paths:
        if not os.path.exists(path):
            continue
        snippets += __getWantSnippets(path)
    return snippets


def wantSnippet(snippet, emitter_type="python"):
    """ Locate the specified snippet and want it.
    """
    logger.debug("Called wantSnippet(%s, %s)..." % (snippet, emitter_type))

    __emitCommandsForShell(snippet, emitter_type)


def unwantSnippet(snippet, emitter_type="python"):
    """ Unwant the snippet, reversing it's effects.
    """
    logger.debug("Called unwantSnippet(%s, %s)..." % (snippet, emitter_type))

    __emitCommandsForShell(snippet, emitter_type, should_unwant=True)


def whichSnippet(snippet):
    """ Show which snippet would be used.
    """
    logger.debug("Called whichSnippet(%s)..." % snippet)
    snippet_path = __findSnippet(snippet)
    return snippet_path


def whereSnippet(snippet):
    """ Show which snippets (note the plural) would be used, in order
        of precedence.
    """
    logger.debug("Called whereSnippet(%s)..." % snippet)


def wantedSnippets(snippet):
    """ Generate a list of snippets that have been wanted.
    """
    logger.debug("Called wantedSnippet(%s)..." % snippet)


def parseSnippet(snippet):
    """ Parse the snippet name.
    """
    logger.debug("Called parseSnippet(%s)..." % snippet)

    snippet = re.sub(r'\.want$', '', snippet)
    name_part, version_part = string.split(snippet, '-', maxsplit=2)
    return name_part, version_part


# ---------------------------------------------------------------------------------------------
# Private code
# ---------------------------------------------------------------------------------------------
def __getWantPaths():
    """ Get the list of paths to search for want snippets.
    """
    if not 'UTONIUM_WANT_PATH' in os.environ:
        msg = "Environment variable 'UTONIUM_WANT_PATH' is not set, unable to search for want snippets..."
        raise WantError(msg)

    paths = list()
    for path in string.split(os.environ['UTONIUM_WANT_PATH'], os.pathsep):
        path = os.path.expanduser(path)
        path = os.path.normpath(path)
        paths.append(path)
    return paths


def __getWantSnippets(path, with_full_path=False):
    """ Get the list of want snippets that reside in the specified location.
    """
    snippets = list()
    items = os.listdir(path)
    for item in items:
        if re.search(r'^\w+\-([\w\.]+)\.want$', item):
            snippets.append(re.sub(r'\.want$', '', item))
    return snippets


def __findSnippet(desired_snippet):
    """ Locate the specified snippet.
    """
    desired_snippet = re.sub(r'\.want$', '', desired_snippet)

    snippet_path = None
    for path in __getWantPaths():
        if not os.path.exists(path):
            continue
        for snippet in __getWantSnippets(path):
            if desired_snippet == snippet:
                snippet_path = os.path.join(path, snippet + ".want")
                break
        if snippet_path: break
    return snippet_path


def __walkSnippet(snippet, recurse=True):
    """ Open the snippet, parse it's contents, and process it.
    """
    logger.debug("Walking snippet '%s'..." % snippet)

    commands = list()

    snippet_path = __findSnippet(snippet)
    if snippet_path:
        fh = open(snippet_path)
        contents = fh.readlines()
        fh.close()

        for line in contents:
            if re.search(r'^\s*$', line): continue

            cmd = __parseLine(line, snippet_path)
            logger.debug("Command action: %s" % cmd['action'])
            logger.debug("Command params: %s" % cmd['params'])

            if cmd['action'] == emitters.base.ACTION_WANT:
                if recurse:
                    commands += __walkSnippet(cmd['params'][0])
                    continue
            else:
                commands.append(cmd)
    else:
        msg = "Unable to find snippet '%s'" % snippet
        raise WantError(msg)


    return commands


def __parseLine(line, snippet_path):
    """ Parse the line from the want snippet.
    """
    action = None
    params = list()
    if re.search(r'\s', line):
        line = string.strip(line)
        parts = re.split(r'\s+', line)
        action = parts[0]
        params = parts[1:]
    else:
        action = line

    if not action in emitters.base.VALID_ACTIONS:
        msg = "Unknown action '%s' in snippet '%s'" % (action, snippet_path)
        raise WantError(msg)

    # TODO: Make sure the command has enough parameters.

    cmd = dict()
    cmd['action'] = action
    cmd['params'] = params
    return cmd


def __emitCommandsForShell(snippet, emitter_type, should_unwant=False):
    """ Emit the commands for the specified emitter type.
    """
    # TODO: Emit commands to update the following env var.
    #    if not 'UTONIUM_WANTED_SNIPPETS' in os.environ:
    #        print("GOT HERE 1")
    #        os.environ['UTONIUM_WANTED_SNIPPETS'] = snippet
    #    else:
    #        print("GOT HERE 2")
    #        os.environ['UTONIUM_WANTED_SNIPPETS'] = os.environ['UTONIUM_WANTED_SNIPPETS'] + os.pathsep + snippet

    commands = __walkSnippet(snippet)

    emitter = emitters.spawnEmitter(emitter_type, commands)
    emitter.emit(unwant=should_unwant)


# ---------------------------------------------------------------------------------------------
# Errors
# ---------------------------------------------------------------------------------------------
class WantError(Exception):
    pass


# ---------------------------------------------------------------------------------------------
# Module test harness
# ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(0)
