#!/bin/sh
set -x
#seq-gen -mHKY -n1000 -or tree.txt > simdata.txt || exit
python phylip2json.py simdata.txt > simdata.json || exit
echo 'Succeeded'