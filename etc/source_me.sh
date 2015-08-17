#!/bin/sh
#
# source_me.sh
#
# Copyright Kevin Cureton
#

# Figure out what kind of OS this is. Used to find any compiled things.
# Thinking forward to a compiled version of pathmod.
export UTONIUM_WANT_OS=`uname -s`
export UTONIUM_WANT_ARCH=`uname -m`
export UTONIUM_WANT_OSARCH="${UTONIUM_WANT_OS}.${UTONIUM_WANT_ARCH}"

# The location where want lives.
#export UTONIUM_WANT_ROOT=${UTONIUM_WANT_ROOT:="~/Documents/work/github/want"}
export UTONIUM_WANT_ROOT=${UTONIUM_WANT_ROOT:="/opt/utonium/want"}

# Necessary paths added the old-fashion way. It's safe to assume PATH is
# already set. Bigger problems exist if it isn't. :)
export PATH="${UTONIUM_WANT_ROOT}/bin:${PATH}"

# Give Python some initial config so scripts can find want Python modules.
export PYTHONPATH=`pathmod --append PYTHONPATH ${UTONIUM_WANT_ROOT}/src/python`

# New want paths. Snippets included with the source are added at the
# end of the list.
export UTONIUM_WANT_PATH=`pathmod --append UTONIUM_WANT_PATH ${UTONIUM_WANT_ROOT}/snippets`

test -e ${HOME}/want
if [ $? == 0 ]; then
    # Goes on the list first. Which means anything in your ${HOME}/want will be
    # found first by the want command.
    export UTONIUM_WANT_PATH=`pathmod --prepend UTONIUM_WANT_PATH ${HOME}/want`
fi

# Initialize the environment variable that will track what snippets
# have been wanted.
export UTONIUM_WANTED_SNIPPETS=""

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
