import os
import sys
import time
from stat import ST_SIZE
from ulogstash.inputs import base

class File(base.Input):
    def follow(self, filename):
        fd = open(filename, 'r')
        file_len = os.stat(filename)[ST_SIZE]
        fd.seek(file_len)
        while True:
            try:
                pos = fd.tell()
                line = fd.readline()
                if not line:
                    if os.stat(filename)[ST_SIZE] < pos:
                        fd.close()
                        fd = open(filename, 'r')
                        continue
                    time.sleep(0.1)
                    fd.seek(pos)
                    continue
                yield line
            except (KeyboardInterrupt, SystemExit):
                print "Exiting..."
                break
