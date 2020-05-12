#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    l=[]
    for i in s:
        if not l:
            l.append(i)
        else:
            if l[-1]==i:
                l.pop()
            else:
                l.append(i)
    if not l:
        return 'Empty String'
    return "".join(l)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
