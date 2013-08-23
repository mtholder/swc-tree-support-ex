#!/usr/bin/env python
'''
Takes file with one integer per line.

Writes the smallest integer that is greater than at least 95% of the numbers.

For the input:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
25

The output should be:
20

because 20 is bigger than the first 19 out of the 20 entries

Note that we'd expect the same output for 

25
0
0
0
0
0
0
0
0
0
0
0
19
0
0
0
0
0
0
0

'''

import sys

filename = sys.argv[1]
inp = open(filename, 'rU')
