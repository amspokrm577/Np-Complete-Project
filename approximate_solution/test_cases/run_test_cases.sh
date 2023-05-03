#!/bin/bash

echo "----------------"
echo "Running all tests..."

#Test 1, whole graph is max clique
#6 vertices, 15 edges
echo "----------------"
echo "TEST 1: "
echo -e $divider
expectedoutput="1 2 3 4 5 6"
echo "Expected Output:"
echo $expectedoutput
echo -e $divider
echo "Actual Output: $test1"
test1= /usr/bin/time -f "\nRun time: %e sec" python cs412_maxclique_approx.py < input1.txt
echo $test1
if [ "$test1" == "$expected" ]
then
    echo "Test Passed"
else
    echo "Test did not Pass"
fi

#Test 2
#16 vertices, 41 edges
#RT: .05 sec
echo "----------------"
echo "TEST 2: "
expectedoutput="1 2 3 4 5 6 7 8"
echo -e $divider
echo "Expected output: "
echo $expectedoutput
echo -e $divider
echo "Actual Output: $test1"
test2= /usr/bin/time -f "\nRun time: %e sec" python cs412_maxclique_approx.py < input2.txt
echo $test2
if [ "$test2" == "$expected" ]
then
    echo "Test Passed"
else
    echo "Test did not Pass"
fi

#Test 3
#25 vertices, 204 edges
echo "----------------"
echo "TEST 3: "
expectedoutput="2 1 3 4 5 6 10 11 12 13 14 15 16 17 18 7 9 20 19 8"
echo -e $divider
echo "Expected output: "
echo $expectedoutput
echo -e $divider
echo "Actual Output: "
test3= /usr/bin/time -f "\nRun time: %e sec" python cs412_maxclique_approx.py < input3.txt
echo $test3
if [ "$test3" == "$expected" ]
then
    echo "Test Passed"
else
    echo "Test did not Pass"
fi

#Test 4
#73 vertices, 99 edges
echo "----------------"
echo "TEST 4: "
expectedoutput="0 1 2 3 4"
echo -e $divider
echo "Expected output: "
echo $expectedoutput
echo -e $divider
echo "Actual Output: "
test4= /usr/bin/time -f "\nRun time: %e sec" python cs412_maxclique_approx.py < input4.txt
echo $test4
if [ "$test4" == "$expected" ]
then
    echo "Test Passed"
else
    echo "Test did not Pass"
fi

#Test 5
#29 vertices, 223 edges
echo "----------------"
echo "TEST 5: "
expectedoutput="4 5 19 3 16 9 6 1 14 10 12 11 8 13"
echo -e $divider
echo "Expected output: "
echo $expectedoutput
echo -e $divider
echo "Actual Output: "
test5= /usr/bin/time -f "\nRun time: %e sec" python cs412_maxclique_approx.py < input5.txt
echo $test5
if [ "$test5" == "$expected" ]
then
    echo "Test Passed"
else
    echo "Test did not Pass"
fi

#Test 6
#12 vertices, 50 edges
echo "----------------"
echo "TEST 6: "
expectedoutput="9 7 3 1 6"
echo -e $divider
echo "Expected output: "
echo $expectedoutput
echo -e $divider
echo "Actual Output: "
test5= /usr/bin/time -f "\nRun time: %e sec" python cs412_maxclique_approx.py < input6.txt
echo $test5
if [ "$test5" == "$expected" ]
then
    echo "Test Passed"
else
    echo "Test did not Pass"
fi

#Test 7
#22 vertices, 49 edges
echo "----------------"
echo "TEST 7: "
expectedoutput="0 1 2 3 4"
echo -e $divider
echo "Expected output: "
echo $expectedoutput
echo -e $divider
echo "Actual Output: "
test5= /usr/bin/time -f "\nRun time: %e sec" python cs412_maxclique_approx.py < input7.txt
echo $test5
if [ "$test5" == "$expected" ]
then
    echo "Test Passed"
else
    echo "Test did not Pass"
fi

#Test 8
#55 vertices, 120 edges
echo "----------------"
echo "TEST 8: "
expectedoutput="0 1 2 3 4"
echo -e $divider
echo "Expected output: "
echo $expectedoutput
echo -e $divider
echo "Actual Output: "
test5= /usr/bin/time -f "\nRun time: %e sec" python cs412_maxclique_approx.py < input8.txt
echo $test5
if [ "$test5" == "$expected" ]
then
    echo "Test Passed"
else
    echo "Test did not Pass"
fi

#Test 9
#35 vertices, 89 edges
echo "----------------"
echo "TEST 9: "
expectedoutput="3 4 8 11 2 10 9 6 5 1 7"
echo -e $divider
echo "Expected output: "
echo $expectedoutput
echo -e $divider
echo "Actual Output: "
test5= /usr/bin/time -f "\nRun time: %e sec" python cs412_maxclique_approx.py < input9.txt
echo $test5
if [ "$test5" == "$expected" ]
then
    echo "Test Passed"
else
    echo "Test did not Pass"
fi

