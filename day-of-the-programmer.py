#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    if (year%400==0) or (year%4==0 and year%100!=0) or year==1800 or year==1900 or year==1700 :
        return ("12.09."+str(year))
    if (year==2100):
        return ("13.09."+str(year))
    if (year==1918):
        return("26.09."+str(year))
    else:
        return("13.09."+str(year))
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
