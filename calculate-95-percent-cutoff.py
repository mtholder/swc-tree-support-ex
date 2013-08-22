#!/usr/bin/env python
'''
Takes file with one integer per line.

Writes the smallest integer that is greater than at least 95% of the numbers.
'''

import sys

filename = sys.argv[1]
inp = open(filename, 'rU')
