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

import socket
import threading
import SocketServer

from globals import (HOME_IP, HOME_PORT)

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        response = "{}: {}".format(cur_thread.name, data)
        self.request.sendall(response)


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass


def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message)
        response = sock.recv(1024)
        print "Received: {}".format(response)
    finally:
        sock.close()


if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 0
    ip = HOME_IP
    port = HOME_PORT
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running in thread:", server_thread.name

