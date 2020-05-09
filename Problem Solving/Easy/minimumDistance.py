#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    lst=[]
    n=0
    for i in a:
        if a.count(i)>1:
            firstPos=a.index(i)
            secondPos=a.index(i, firstPos+1)
            lst.append(secondPos-firstPos)
    if not lst:
        lst.append(-1)
    return min(lst)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
