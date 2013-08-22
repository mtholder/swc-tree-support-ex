#!/bin/sh
set -x

seq-gen -mHKY -n1000 -or tree.txt > simdata.txt 2>seq-gen-err-stream.txt || exit

python rel-phylip2json.py simdata.txt > simdata.json || exit

set +x 
echo 'Success!'