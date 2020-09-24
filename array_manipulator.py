#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    my_array = []
    [my_array.append(0) for _ in range(n)]
    for row in range(len(queries)):
        a=queries[row][0]-1
        b=queries[row][1]-1
        k=queries[row][2]     
        for x in range(0,len(my_array)):
            if a<=x<=b:
                my_array[x]+=k

    return max(my_array)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

