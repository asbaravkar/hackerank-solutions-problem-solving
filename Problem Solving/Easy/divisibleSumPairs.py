#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    c=0
    for i in range(n):
        lst=[]
        lst.append(ar[i])
        for j in range(i+1,n):
            lst.append(ar[j])
            # print(lst)
            if sum(lst)%k==0:
                c+=1
            lst.pop(-1)
    return c        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()