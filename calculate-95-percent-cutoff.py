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

# parse the input into a list of ints
value_list = []
for line in inp:
    value = int(line.strip())
    value_list.append(value)

# Sort the list, smallest to largest
# After this the number 95% of the way through the list will be
# the critical value
value_list.sort()

num_values = len(value_list)

# this is a bit sloppy, we'll just round and then make the 
#   index an int
critical_index_float = 0.95*num_values
critical_index_rounded_up = round(critical_index_float)
critical_index = int(critical_index_rounded_up)

assert critical_index > 0
# decrement so that the index starts at 0
critical_index -= 1

# we add one because we were told to calculate a value that is
# greater than 95 % 
print(1 + value_list[critical_index])


