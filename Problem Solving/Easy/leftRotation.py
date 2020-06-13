#!/bin/python3

import math
import os
import random
import re
import sys

def rotate(a, d):
    while(d!=0):
        t=a.pop(0)
        a.append(t)
        d=d-1
    for i in a:
        print(i,end=" ")

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotate(a,d)
