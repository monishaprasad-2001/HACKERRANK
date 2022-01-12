#!/bin/python3

from math import gcd
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def get_hcf(arr):
    hcf = arr[0] 
    for i in arr:
        hcf = gcd(hcf,i)
    return hcf

def lcm(a,b):
    return a*b//gcd(a,b)

def get_lcm(arr):
    l = arr[0] 
    for i in arr:
        l = lcm(l,i)
    return l

def getTotalX(a,b):
    lcm_a = get_lcm(a)
    hcf_b = get_hcf(b)
    no_between_sets = sum(1 for i in range(lcm_a, hcf_b+1, lcm_a) if not hcf_b%i and i%lcm_a==0)
    return no_between_sets

    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
