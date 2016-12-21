#!/usr/bin/env python
# -*- encoding: UTF8 -*-


"""
Write data in "chunks" to a file on the filesystem.
  - `chunk_size` should be configurable.
  - Set a minimum `chunk_size` of 10 MB
  - Start each client with a different chunk size (random).
  - When the data file size reaches the configurable chunk_size,
    rollover the data file, IE:
    stop writing, save file, start writing to a new file.
  - Warning on startup if the run time configured and the "chunk" size
    configured do not allow you to rollover a minimum of 2 times.
  - When a data file rolls over:
    - log to the client
    - Send a message to the server
"""

import sys

blocksize = int(sys.argv[1])

chunk = b'\xff' * 10000
with open("file.file", "wb") as f:
    for _ in range(blocksize // 10000):
        f.write(chunk)

"""
refs:
https://github.com/sanderjo/disk-speed/blob/master/diskspeed.py
http://blog.philippklaus.de/2009/12/testing-the-data-rate-of-a-hard-disk-using-dd-here-the-samsung-sp2504c-250gb/

"""


def main():
    pass

if __name__ == '__main__':
    main()
