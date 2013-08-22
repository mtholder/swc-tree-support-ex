#!/usr/bin/env python
'''Reads a JSON file with an array 
of 4-sequence character matrices.

Writes 3 counts for each matrix separated by a space in the order:

count_first_second count_first_third count_first_last

where count_first_second is the number of positions in the 'data' strings
of the matrix at which:
    datum for the first row == datum for the second row
  AND
    datum for the third row == datum for the last row
  AND
    datum for the first row != datum for the third row



The other counts are defined similarly for this notion of 
shared data states. This type of shared data between first and third row 
(reported in the slot for count_first_third) and between the first 
and last row (reported in the column for count_first_last)

So a single data matrix:

CGACCAGGTATG
CGACCAGGTACG
CCGTCCGGTCTG
CCGCCTGGTCCG

would be represented as:

[
    [
        {
            "name":"human", 
            "data" :"CGACCAGGTATG"
        },
        {
            "name":"chimp",
            "data" :"CGACCAGGTACG"
        },
        {
            "name":"gorilla", 
            "data" :"CCGTCCGGTCTG"
        },
        {
            "name":"orang", 
            "data" :"CCGCCTGGTCCG"
        }
    ]
]

in JSON. Running that matrix through this script should result
in the output line:

3 1 0


'''
import json
import sys
filename = sys.argv[1]
inp = open(filename, 'rU')
matrix_list = json.load(inp)

for curr_matrix in matrix_list:
    first_data_str = curr_matrix[0]['data']
    second_data_str = curr_matrix[1]['data']
    third_data_str = curr_matrix[2]['data']
    last_data_str = curr_matrix[3]['data']
    # We expect each string to be the same length. Exit if this is not true...
    assert len(first_data_str) == len(second_data_str)
    assert len(first_data_str) == len(third_data_str)
    assert len(first_data_str) == len(last_data_str)
    # Here is where you'll need to add the
    # code for calculating the 3 counts for the current
    # matrix in the curr_matrix variable and printing out 
    # those counts