#!/usr/bin/python

import sys
import time

timestr=time.strftime("%Y%M%d")
print timestr

#file is given after the script
#read.py file.txt

file=sys.argv[1]
with open(file) as ln :
    line=ln.readline()
    cnt=1
    while line:
        print("Line {}: {}".format(cnt,line.strip()))
        line=ln.readline()
        cnt+=1
