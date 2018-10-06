#!/usr/bin/python

import sys
import time

timestr=time.strftime("%Y%M%d")
print timestr

file='iptest.txt'
with open(file) as ln :
    line=ln.readline()
    cnt=1
    while line:
        print("Line {}: {}".format(cnt,line.strip()))
        line=ln.readline()
        cnt+=1
