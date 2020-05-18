#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    fmap = {}
    for idx,val in enumerate(cost):
        remain = money - val
        if remain in fmap:
            l = sorted([fmap[remain], idx])
        if not remain in fmap:
            fmap[val] = idx
    print(l[0]+1, l[1]+1)

    
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
