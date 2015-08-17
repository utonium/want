#!/bin/tcsh
#
# source_me.tcsh
#
# Copyright Kevin Cureton
#

# Figure out what kind of OS this is. Used to find any compiled things.
# Thinking forward to a compiled version of pathmod.
setenv UTONIUM_WANT_OS `uname -s`
setenv UTONIUM_WANT_ARCH `uname -m`
setenv UTONIUM_WANT_OSARCH "${UTONIUM_WANT_OS}.${UTONIUM_WANT_ARCH}"

# The location where want lives.
#setenv UTONIUM_WANT_ROOT "~/Documents/work/github/want"
setenv UTONIUM_WANT_ROOT "/opt/utonium/want"

# Necessary paths added the old-fashion way. It's safe to assume PATH is
# already set. Bigger problems exist if it isn't. :)
setenv PATH "${UTONIUM_WANT_ROOT}/bin:${PATH}"

# Give Python some initial config so that pathmod can run.
setenv PYTHONPATH `pathmod --prepend PYTHONPATH ${UTONIUM_WANT_ROOT}/src/python`

# New want paths. Snippets included with the source are added at the
# end of the list.
setenv UTONIUM_WANT_PATH `pathmod --append UTONIUM_WANT_PATH ${UTONIUM_WANT_ROOT}/snippets`

test -e ${HOME}/want
if ( $? == 0 ) then
    # Goes on the list first. Which means anything in your ${HOME}/want will be
    # found first by the want command.
    setenv UTONIUM_WANT_PATH `pathmod --prepend UTONIUM_WANT_PATH ${HOME}/want`
endif

# Initialize the environment variable that will track what snippets
# have been wanted.
setenv UTONIUM_WANTED_SNIPPETS ""

# Special aliases.
alias want "source ${UTONIUM_WANT_ROOT}/bin/want.tcsh"
alias unwant "source ${UTONIUM_WANT_ROOT}/bin/unwant.tcsh"
alias wanted "_want --wanted"

# Special completetions.
complete want 'p/1/`_want --list_tcsh`/'
complete unwant 'p/1/`echo $UTONIUM_WANTED_PACKAGES | tr ":" " "`/'
