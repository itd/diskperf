#!/usr/bin/env python
# -*- encoding: UTF8 -*-

"""
report a "heartbeat" status to the server at ~ 5 second intervals.
"""

import socket
from time import sleep
import random

from globals import (HOME_IP, HOME_PORT, HEARTBEAT)


def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))

    try:
        sock.sendall(message)
        response = sock.recv(1024)
        # need to set up logging for this
        print "Received: {}".format(response)

    finally:
        sock.close()

if __name__ == "__main__":
    # ~ around 5 seconds. Add some randomness.
    heartbeat_interval = random.random() + HEARTBEAT - 0.5

    client(HOME_IP, HOME_PORT, "HEARTBEAT:")

