#!/usr/bin/python3

import sys
from os.path import exists

if (len(sys.argv) < 3):
    print("Usage: ./markdown2html.py README.md README.html")
    exit(1)

elif (not exists(sys.argv[1])):
    print(f"Missing {sys.argv[1]}")
    exit(1)

else:
    exit(0)
