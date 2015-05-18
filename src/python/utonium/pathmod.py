#!/usr/bin/env python
"""
pathmod

Core module for the command-line tool of the same name. pathmod's purpose is to manipulate
colon-separated string, which are typically used to store lists of paths in the environment.

Copyright 2015 Kevin Cureton
"""
# ---------------------------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------------------------
import logging
import string
import sys
import os.path

# ---------------------------------------------------------------------------------------------
# Globals
# ---------------------------------------------------------------------------------------------
logger = logging.getLogger()

ACTION_PREPEND = "prepend"
ACTION_APPEND = "append"
ACTION_DELETE = "delete"

ACTIONS = set([
    ACTION_PREPEND,
    ACTION_APPEND,
    ACTION_DELETE
])

# ---------------------------------------------------------------------------------------------
# Code
# ---------------------------------------------------------------------------------------------
def modifyPathsForEnvVar(action, env_var_name, path, should_set_env_var=False):
    """ Modify the set of paths for the given environment variable
        and returns a string to be used to set the environment variable.
    """
    logger.debug("Modifying path for '%s' with action '%s' (%s)..." % (env_var_name, action, path))

    if action not in ACTIONS:
        msg = "Invalid action specified for modifying '%s' paths" % env_var_name
        raise PathmodError(msg)

    if action == ACTION_PREPEND:
        modified_paths = prependPathToEnvVar(env_var_name, path)
    elif action == ACTION_APPEND:
        modified_paths = appendPathToEnvVar(env_var_name, path)
    elif action == ACTION_DELETE:
        modified_paths = deletePathFromEnvVar(env_var_name, path)

    joined_paths = ""
    if len(modified_paths) == 1:
        joined_paths = modified_paths[0]
    elif len(modified_paths) > 1:
        joined_paths = string.join(modified_paths, os.path.pathsep)

    if should_set_env_var:
        os.environ[env_var_name] = joined_paths

    return joined_paths


def prependPathToEnvVar(env_var_name, path_to_prepend):
    """ Prepend the path to the environment variable's value.
    """
    path_to_prepend = os.path.normpath(path_to_prepend)
    modified_paths = deletePathFromEnvVar(env_var_name, path_to_prepend)
    modified_paths.insert(0, path_to_prepend)
    return modified_paths

 
def appendPathToEnvVar(env_var_name, path_to_append):
    """ Append the path to the environment variable's value.
    """
    path_to_append = os.path.normpath(path_to_append)
    modified_paths = deletePathFromEnvVar(env_var_name, path_to_append)
    modified_paths.append(path_to_append)
    return modified_paths

 
def deletePathFromEnvVar(env_var_name, path_to_delete):
    """ Delete the path from the environment variable's value.
    """
    existing_paths = getEnvVarPaths(env_var_name)

    path_to_delete = os.path.normpath(path_to_delete)

    modified_paths = list()
    for path in existing_paths:
        if os.path.normpath(path) != path_to_delete:
            modified_paths.append(path)
    return modified_paths


def hasPathInEnvVar(env_var_name, path):
    """ Whether or not the specified environment variable contains
        the path.
    """
    has_path = False
    paths = getEnvVarPaths(env_var_name)
    if path in set(paths):
        has_path = True
    return has_path


def getEnvVarPaths(env_var_name):
    """ Get the list of paths from the specified environment
        variable name.
    """
    env_paths = list()
    if env_var_name in os.environ:
        if len(os.environ[env_var_name]):
            env_paths = string.split(os.environ[env_var_name], os.path.pathsep)
    return env_paths


class PathmodError(Exception):
    pass


# ---------------------------------------------------------------------------------------------
# Module test harness
# ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(0)
