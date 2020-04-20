#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    leap="12.09."
    non_leap="13.09."
    if year==1918:
        return '26.09.1918'
    elif year>1918 and year%400==0 or year%4==0 and year%100!=0 or year<=1917 and year%4==0:
        return leap+str(year)
    else:
        return non_leap+str(year)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
