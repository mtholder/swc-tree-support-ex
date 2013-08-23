#!/bin/sh
script=calculate-support-from-counts.py
subdir=support-from-counts

total=0
passed=0
echo "testing ${script}"

# run the test for all files in the input dir of the subdirectory of interest...
for path in $(ls tests/${subdir}/input/*)
do
    # set some variables to make the invocation easier to read
    #
    filename=$(basename "${path}")
    input="tests/${subdir}/input/${filename}"
    output="tests/${subdir}/output/${filename}"
    reference="tests/${subdir}/expected-output/${filename}"
    
    # run the script
    #
    echo "testing: python ${script} ${input}"
    if python "${script}" "${input}" > "${output}"
    then
        # If it did not exit with an error, compare
        # the output produced to the expected "reference" output
        #
        if diff "${output}" "${reference}"
        then
            # diff will succeed if the files are identical
            #
            echo "Passed"
            passed=$(expr $passed + 1)
        else
            echo "Did not create the expected output!"
        fi
    else
        echo "Program failed to exit cleanly"
    fi
    total=$(expr $total + 1)
done

echo "Passed $passed out of $total tests"

if test $passed -eq $total
then
    exit 0
else
    exit 1
fi