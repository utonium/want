#!/bin/sh
#
# source_me.sh
#
# Copyright Kevin Cureton
#

umask 002

# Figure out what kind of OS this is...
export UTONIUM_WANT_OS=`uname -s`
export UTONIUM_WANT_ARCH=`uname -m`
export UTONIUM_WANT_OSARCH="${UTONIUM_WANT_OS}.${UTONIUM_WANT_ARCH}"

# The location where want lives.
#export UTONIUM_WANT_ROOT=${UTONIUM_WANT_ROOT:="/opt/utonium/want"}
export UTONIUM_WANT_ROOT=${UTONIUM_WANT_ROOT:="~/Documents/work/github/want"}

# Necessary paths.
export PATH="${UTONIUM_WANT_ROOT}/bin:${PATH}"

# Give Python some initial config so that pathmod can run.
# TODO: Check to make sure it isn't already set.
export PYTHONPATH="${UTONIUM_WANT_ROOT}/src/python:${PYTHONPATH}"

# New want paths. These go on first to have highest precedence.
export UTONIUM_WANT_PATH=`pathmod UTONIUM_WANT_PATH --append ${UTONIUM_WANT_ROOT}/snippets`

test -e ${HOME}/want
if [ $? == 0 ]; then
    export UTONIUM_WANT_PATH=`pathmod UTONIUM_WANT_PATH --prepend ${HOME}/want`
fi

# Special aliases.
alias want="source ${UTONIUM_WANT_ROOT}/bin/want.sh"
alias unwant="source ${UTONIUM_WANT_ROOT}/bin/unwant.sh"
alias wanted="_want --wanted"

# Special completetions.
function want_complete() {
    local word=${COMP_WORDS[COMP_CWORD]}
    local my_list=`_want --list`
    COMPREPLY=($(compgen -W "${my_list}" -- ${word}))
}
complete -F want_complete want

function unwant_complete() {
    local word=${COMP_WORDS[COMP_CWORD]}
    local my_list=`echo $UTONIUM_WANTED_PACKAGES | tr ":" " "`
    COMPREPLY=($(compgen -W "${my_list}" -- ${word}))
}
complete -F unwant_complete unwant
