#!/usr/bin/python

import sys

file_=sys.argv[1]
col=int(sys.argv[2])

#f = sys.stdin
# If you need to open a file instead:
f = open(file_)
##### check how many column
line_ = f.readline()
colnum=len(line_.split())
print colnum,"Columns"
print ''

##### print column
for line in f:
    fields = line.strip().split()
    # Array indices start at 0 unlike AWK
    if col < colnum :
        print(fields[col])
    else :
        exit()
       # print "Nooo"

f.close()
