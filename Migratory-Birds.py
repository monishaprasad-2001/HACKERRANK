#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    sett=[]
    for i in range(len(arr)):
        if arr[i] not in sett:
            sett.append(arr[i]) 

    l=[]
    for i in range(len(sett)):
        count=0
        for j in range(len(arr)):
            if sett[i]==arr[j]:
                count+=1
        l.append(count)
    print(l)
    
    el=[]
    for i in range(len(l)):
        if l[i]==max(l):
            el.append(sett[i])
    return min(el)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
