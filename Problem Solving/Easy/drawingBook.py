#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if n%2==0 and p==n//2:
        return p//2
    if n%2==0 and n-p==1:
        return 1
    diff = n-p
    if diff < p:
        return diff//2
    return p//2
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
