#!/bin/sh
#
# unwant.sh
#
# Copyright 2015 Kevin Cureton

WANT_TMPFILE=`mktemp -t want_commands.XXXXXX.sh`

_want --unwant ${1} sh >${WANT_TMPFILE} 2>&1
. ${WANT_TMPFILE}

/bin/rm -f ${WANT_TMPFILE}
