#!/usr/bin/python

import sys,collections

file_=sys.argv[1]
col=int(sys.argv[2])

f = open(file_)
##### check how many column
line_ = f.readline()
colnum=len(line_.split())

with open(file_) as f:
        counts=(sum(1 for _ in f))
f.close()

print ">",colnum," Columns"
print ">",counts,"Lines"

##### print column
sys.stdout.write("> Print column : %s"%col);sys.stdout.flush();print '\r'
for line in open(file_): 
    fields = line.strip().split()
    # Array indices start at 0 unlike AWK
    if col < colnum :
        print(fields[col])
    else :
        print "No Columns"; exit()
f.close()
