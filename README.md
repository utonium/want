# want
The Want System. Tools for easily pulling in (and subsequently removing) snippets of shell environment into the current process space.

Example Usage
======================

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
