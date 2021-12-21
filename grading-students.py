#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    rounds=0
    finall = []
    for i in range(len(grades)):
        if grades[i]<38:
            finall.append(grades[i])
        elif grades[i]>=38:
            if (grades[i]%5==0):
                finall.append(grades[i])
            else:
                rounds = grades[i] + (5-grades[i]%5)
                if (rounds - grades[i])<3:
                    finall.append(rounds)
                elif (rounds - grades[i]>=3):
                    finall.append(grades[i])
    return finall
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
