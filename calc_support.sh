#!/bin/sh
# set -x makes bash print each line to the standard error stream
#    before executing it. This is handy for debugging
set -x

python calculate-shared-counts.py data/simdata.json > counts.txt || exit

python calculate-support-from-counts.py counts.txt > support-values.txt || exit

python calculate-95-percent-cutoff.py support-values.txt || exit
