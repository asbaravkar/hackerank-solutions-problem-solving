#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    l=[]
    f=[]
    c=0
    for i in range(len(s)-2):
        l.append([s[i],s[i+1],s[i+2]])
    for i in range(0,len(l),3):
        f.append(l[i])

    for lst in f:
        if lst[0]!='S':
            c+=1
        if lst[1]!='O':
            c+=1
        if lst[2]!='S':
            c+=1
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
