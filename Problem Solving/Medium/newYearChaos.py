#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    c=0
    for index in range(len(q)-1, 0, -1): # iterating from back
        if(q[index]!=index+1): # last element is not at its right position & bribe has occured
            if(q[index-1]==index+1): # whether last element is at second last position
                c+=1
                
                q[index-1],q[index]=q[index],q[index-1] # swap last & secondlast
            elif(q[index-2]==index+1): # third last position checking
                c+=2
                q[index-2],q[index-1]=q[index-1],q[index-2] # swap thirdlast & secondlast
                q[index],q[index-1]=q[index-1],q[index] # swap secondlast & last
            else:
                return "Too chaotic"
    return c
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
