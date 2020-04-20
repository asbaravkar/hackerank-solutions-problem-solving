#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    high_score,low_score=scores[0],scores[0]
    high,low=0,0
    for i in range(len(scores)):
        if scores[i]>high_score:
            high_score=scores[i]
            high+=1
        if scores[i]<low_score:
            low_score=scores[i]
            low+=1
    return [high,low]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
