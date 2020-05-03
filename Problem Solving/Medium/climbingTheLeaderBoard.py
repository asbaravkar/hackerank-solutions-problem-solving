#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    # to append final scores after comparing
    lst = []
    # to start from index left from previous iteration
    counter = 0
    #unique sorted scores
    scores = sorted(list(set(scores))) 
    
    for i in alice:
        while(counter < len(scores) and i >= scores[counter]):
                # check next score
                counter+=1
        # out of loop means i < scores[counter]
        lst.append(len(scores)-(counter-1))
    return lst
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
