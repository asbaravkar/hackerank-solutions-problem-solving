#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    people = 5
    like = []
    for day in range(n):
        liked = math.floor(people/2)
        people = liked*3
        like.append(liked)
    return sum(like)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
