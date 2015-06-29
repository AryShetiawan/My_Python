#!/usr/bin/env python

import sys
import time

if len(sys.argv) != 2:
    sys.exit("usage: use_memory <number-of-gigabytes>")

count = int(sys.argv[1])

gigabyte = (0,) * (1024 * 1024 / 8 * 1000)
data = gigabyte * count
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    e = "goodbye"
except Exception as e:
    pass # handle in finally clause
finally:
    del data
    sys.exit(str(e))
