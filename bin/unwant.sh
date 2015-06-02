#!/bin/sh
#
# unwant.sh
#
# Copyright 2015 Kevin Cureton

WANT_TMPFILE=`mktemp -t want_commands.XXXXXX.sh`

_want --unwant ${1} sh >${WANT_TMPFILE}
. ${WANT_TMPFILE}

/bin/rm -f ${WANT_TMPFILE}
