#!/usr/bin/env python
# -*- encoding: UTF8 -*-

"""
Master/Server Requirements
--------------------------

* Needs to handle concurrent client connections.

* Log the client performance data to log file.

* Logs client "heartbeat" status and other messages to log file.

* When all clients have finished, writes out a report with some
  general usage, if a client went away, perf stats, etc. then exits.

Modules that are not in the python standard library are allowed BUT
you must state so in any help/usage messaging and gracefully handle/
shutdown the client/server when they are not present.  Any such
modules must be easily installable via PIP; no compilation
dependencies.
"""