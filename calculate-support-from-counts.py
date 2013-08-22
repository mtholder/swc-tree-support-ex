#!/usr/bin/env python
'''
Takes a file with rows of integers separated by whitespace.

Writes the difference between the highest number in a row and the 
    second highest number in the row

If the highest number occurs twice, 0 is written to standard output

So the input: 

3 1 0
7 58 50

Should result in the output:

2 
8

'''
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
    inp = open(filename, 'rU')
else:
    inp = sys.stdin

for line in inp:
    word_list = line.strip().split()
    number_list = []
    for word in word_list:
        number = int(word)
        number_list.append(number)
    number_list.sort(reverse=True)
    num_words = len(word_list)
    assert num_words > 1
    biggest = number_list[0]
    next_biggest = number_list[1]
    support = biggest - next_biggest
    print(support)