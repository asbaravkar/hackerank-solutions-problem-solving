#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    lst=[]
    if p==1:
        lst.append(1)
    for i in range(p,q+1):
        sqr=i**2
        s_sqr=str(sqr)
        s_i=str(i)
        n_sqr=len(s_sqr)
        n_i=len(s_i)
        
        right_rev=s_sqr[::-1]
        right_1=right_rev[:n_i]
        right=right_1[::-1]
        
        left=s_sqr[:n_sqr-len(right)]
        
        try:
            if (int(left)+int(right))==i:
                lst.append(i)
        except ValueError as e:
                left=0
    for i in lst:
        print(i, end=" ")

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
