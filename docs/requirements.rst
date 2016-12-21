Python Programming Exercise
=====================================

The customer wants to compare the performance of various storage
solutions on their network. You are tasked with creating a
distributed storage benchmark tool consisting of two parts, a client
and a server. The client program measures the performance of locally
mounted disks and submits the results back to the server.  You will
also need to create a test strategy for testing your solution. All
systems run Ubuntu 14.04 and have Python 2.7 with standard packages
installed.

You can develop on a Mac but we don't want to hear “it runs on my
system” if we can't get it to run on a standard Ubuntu 14.04 install.

Do not use Python3.

Modules that are not in the python standard library are allowed BUT
you must state so in any help/usage messaging and gracefully handle/
shutdown the client/server when they are not present.  Any such
modules must be easily installable via PIP; no compilation
dependencies.

Do your best, do what you can.  If you can't meet all of the
requirements, meet what you can, polish what you have, call out what
you missed and why.  The expectations of junior, mid-level and
senior engineers are different.  For example, we absolutely expect
to see unit tests from more senior candidates.


Master/Server Requirements
--------------------------

* Needs to handle concurrent client connections.

* Log the client performance data to log file.

* Logs client "heartbeat" status and other messages to log file.

* When all clients have finished, writes out a report with some
  general usage, if a client went away, perf stats, etc. then exits.



Slave/Client Requirements
-------------------------

* Minimum of 3 clients running at the same time - they can all be
  running locally.

* Each client should run for a configurable length of time and
  then shut itself down.

* Client should log start/stop messages and those messages will
  need to be sent to the server.

* Each client will have several threads/processes running, with a
    minimum of the following:-

  1. 1st thread/process will write data in "chunks" to a file on
     the filesystem.

    * The "chunk" size should be configurable but some reasonable
      minimum like 10MB.

    * Each client should start with a different "chunk" size.

    * When the data file gets to a configurable size, rollover the
      data file, IE: stop writing, save file, start writing to a new file.

    * The client should complain on startup if the run time
      configured and the "chunk" size configured do not allow you to
      rollover a minimum of 2 times.

    * A message should be logged to the client and a message should
      be sent to the server when a data file rolls over.

  2. 2nd thread/process is to report CPU & memory information on
     the "data" thread/process to the server at approximately 10 second
     intervals.

  3. 3rd thread/process will report a "heartbeat" status to the
     server at approximately 5 second intervals.



