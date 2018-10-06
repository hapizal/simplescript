#!/usr/bin/env python

import re, sys

for line in open('freemem.txt'):
    for l in line:
       # filex=sys.stdout.write(l)
       
        if re.search(sys.argv[1],l):
            sys.stdout.write(l)


#map(sys.stdout.write,(l for l in sys.stdin if re.search(sys.argv[1],l)))
