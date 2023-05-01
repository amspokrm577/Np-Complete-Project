#!/bin/bash

echo "----------------"
echo "Running all tests..."

#Test 1, whole graph is max clique
#6 vertices, 15 edges
#RT: .02 sec
echo "----------------"
echo "TEST 1: "
echo -e $divider
expectedoutput="1 2 3 4 5 6"
echo "Expected Output:"
echo $expectedoutput
echo -e $divider
echo "Actual Output: $test1"
test1= /usr/bin/time -f "\nRun time: %e sec" python maxclique.py < input1.txt
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
test2= /usr/bin/time -f "\nRun time: %e sec" python maxclique.py < input2.txt
echo $test2
if [ "$test2" == "$expected" ]
then
    echo "Test Passed"
else
    echo "Test did not Pass"
fi

#Test 3
#25 vertices, 204 edges
#RT: 65.11 sec
echo "----------------"
echo "TEST 3: "
expectedoutput="2 1 3 4 5 6 10 11 12 13 14 15 16 17 18 7 9 20 19 8"
echo -e $divider
echo "Expected output: "
echo $expectedoutput
echo -e $divider
echo "Actual Output: "
test3= /usr/bin/time -f "\nRun time: %e sec" python maxclique.py < input3.txt
echo $test3
if [ "$test3" == "$expected" ]
then
    echo "Test Passed"
else
    echo "Test did not Pass"
fi

#Test 4
#67 vertices, 99 edges
#RT: 173.37 sec
echo "----------------"
echo "TEST 4: "
expectedoutput="0 1 2 3 4"
echo -e $divider
echo "Expected output: "
echo $expectedoutput
echo -e $divider
echo "Actual Output: "
test4= /usr/bin/time -f "\nRun time: %e sec" python maxclique.py < input4.txt
echo $test4
if [ "$test4" == "$expected" ]
then
    echo "Test Passed"
else
    echo "Test did not Pass"
fi

#Test 5
#29 vertices, 223 edges
#RT: 194.94 sec
echo "----------------"
echo "TEST 5: "
expectedoutput="4 5 19 3 16 9 6 1 14 10 12 11 8 13"
echo -e $divider
echo "Expected output: "
echo $expectedoutput
echo -e $divider
echo "Actual Output: "
test5= /usr/bin/time -f "\nRun time: %e sec" python maxclique.py < input5.txt
echo $test5
if [ "$test5" == "$expected" ]
then
    echo "Test Passed"
else
    echo "Test did not Pass"
fi

#Test 6
#12 vertices, 50 edges
#RT: .03 sec
echo "----------------"
echo "TEST 6: "
expectedoutput="1 3 5 4 6 2"
echo -e $divider
echo "Expected output: "
echo $expectedoutput
echo -e $divider
echo "Actual Output: "
test6= /usr/bin/time -f "\nRun time: %e sec" python maxclique.py < input6.txt
echo $test6
if [ "$test6" == "$expected" ]
then
    echo "Test Passed"
else
    echo "Test did not Pass"
fi

#Test 7
#22 vertices, 49 edges
#RT: 0.17 sec
echo "----------------"
echo "TEST 7: "
expectedoutput="0 1 2 3 4"
echo -e $divider
echo "Expected output: "
echo $expectedoutput
echo -e $divider
echo "Actual Output: "
test7= /usr/bin/time -f "\nRun time: %e sec" python maxclique.py < input7.txt
echo $test7
if [ "$test7" == "$expected" ]
then
    echo "Test Passed"
else
    echo "Test did not Pass"
fi

#Test 8
# 55 vertices, 120 edges
#RT: 55.85 sec
echo "----------------"
echo "TEST 8: "
expectedoutput="0 1 2 3 4"
echo -e $divider
echo "Expected output: "
echo $expectedoutput
echo -e $divider
echo "Actual Output: "
test8= /usr/bin/time -f "\nRun time: %e sec" python maxclique.py < input8.txt
echo $test8
if [ "$test8" == "$expected" ]
then
    echo "Test Passed"
else
    echo "Test did not Pass"
fi

#Test 9
#34 vertices, 89 edges
#RT: 1802.45 sec (Over 20 minutes)
echo "----------------"
echo "TEST 9: "
expectedoutput="4 6 9 11 8 5 3 7 1 2 10"
echo -e $divider
echo "Expected output: "
echo $expectedoutput
echo -e $divider
echo "Actual Output: "
test9= /usr/bin/time -f "\nRun time: %e sec" python maxclique.py < input9.txt
echo $test9
if [ "$test9" == "$expected" ]
then
    echo "Test Passed"
else
    echo "Test did not Pass"
fi
