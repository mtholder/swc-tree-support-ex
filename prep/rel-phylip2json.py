#!/usr/bin/env python
import sys
import re
import json

try:
    filename = sys.argv[1]
except:
    inp = sys.stdin
else:
    inp = open(filename, 'rU')

matrix_list = []
current_matrix = None
matrix_prefix = re.compile(r'^\s*\d+\s\d+')

for line in inp:
    if matrix_prefix.match(line):
        if current_matrix is not None:
            assert len(current_matrix) > 0
            matrix_list.append(current_matrix)
        current_matrix = []
    else:
        name, sequence = line.strip().split()
        row = {'name': name,
               'data': sequence}
        current_matrix.append(row)

assert current_matrix is not None
assert len(current_matrix) > 0
matrix_list.append(current_matrix)

json.dump(matrix_list, sys.stdout, indent=4)