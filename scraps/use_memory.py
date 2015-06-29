#!/usr/bin/env python

import sys
import time

if len(sys.argv) != 2:
    print "usage: use_memory <number-of-gigabytes>"
    sys.exit()

count = int(sys.argv[1])

gigabyte = (0,) * (1024*1024 * 1024 / 8)
data = gigabyte * count

while True:
    time.sleep(1)
