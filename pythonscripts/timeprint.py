#!/usr/bin/python

import time
import os

timestr=time.strftime("%Y%M%d")
print timestr
print "\r"
os.system("date +%Y%M%d")
os.system("uname -r")
