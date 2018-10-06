#!/usr/bin/env python

import re, sys

map(sys.stdout.write,(l for l in sys.stdin if not re.search(sys.argv[1],l)))
