#!/bin/sh
failures=0
if ! sh test_shared_counts.sh
then
    failures=$(expr $failures + 1)
fi

if ! sh test_support_from_counts.sh
then
    failures=$(expr $failures + 1)
fi

if ! sh test_cutoff.sh
then
    failures=$(expr $failures + 1)
fi

if test $failures -gt 0
then
    echo 'Some tests failed (see messages above)'
    exit 1
fi
echo "All tests passed."
