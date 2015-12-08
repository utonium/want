# want
The Want System. Tools for easily pulling in (and subsequently removing) snippets of shell environment into the current process space.

Installation
======================
Check out the git repository into /opt/utonium/want. If you use another location, update the
etc/source_me.* file with the new path.

As part of the shell startup for a user or the shell setup of a service, source the appropriate
file in etc.

    source /opt/utonium/want/etc/source_me.sh

Example Usage
======================

    >> source /opt/utonium/want/etc/source_me.sh

    >> which python
    /usr/bin/python
    >> want python-2.7.9
    >> which python
    >> /opt/my_special_build/bin/python

Tools In Detail
======================

pathmod
----------------------
CLI tool and associated Python module used for modify environment variable path lists.
