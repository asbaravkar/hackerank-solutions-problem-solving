#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.

def birthdays(s,d,m):
    lst=s[:m-1] #take m-1 elements in list
    c=0
    for i in s[m-1:]: # from m-1 elements onwards
        lst.append(i) # add element into list and check sum
        if sum(lst)==d:
            c+=1
        lst.pop(0) # before moving to next iteration pop element at first position
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthdays(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
