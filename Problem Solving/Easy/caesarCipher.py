#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    l=list(s)
    k=k%(ord('z')-ord('a')+1)

    for index,val in enumerate(l):
        if val.isalpha():
            if val.isupper():
                ch=ord(val)+k
                if ch>ord('Z'):
                    ch=ch-ord('Z')-1+ord('A')
                    # print(ch)
                l[index]=chr(ch)
            else:
                ch=ord(val)+k
                if ch>ord('z'):
                    ch=ch-ord('z')-1+ord('a')
                    # print(ch)
                l[index]=chr(ch)    
    return "".join(l)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
