#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    lst=[]
    while(len(arr)!=0):
        c=0
        minimum=min(arr)
        for j in range(len(arr)):
            arr[j] = arr[j] - minimum
            c+=1
        lst.append(c)
        arr = list(filter((0).__ne__, arr))
    return lst

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
