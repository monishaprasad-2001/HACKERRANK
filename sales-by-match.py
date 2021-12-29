#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    socks = set(ar)
    cl=[]
    
    for i in range(len(socks)):
        count=0
        for j in range(len(ar)):
            if list(socks)[i]==ar[j]:
                count += 1
        cl.append(count)
    
    mount = 0
    for c in range(len(cl)):
        if cl[c]>2:
            mount+=cl[c]//2
        if cl[c]==2:
            mount+=1
    return mount
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
