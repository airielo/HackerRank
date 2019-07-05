
import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
sums_list = []
def hourglassSum(arr):
    for row in range(1, len(arr[0])-1):
        for col in range(1, len(arr[1])-1):
            core = arr[row][col]
            topleft = arr[row-1][col-1]
            topright = arr[row-1][col+1]
            topcenter = arr[row-1][col]
            bottomleft = arr[row+1][col-1]
            bottomright = arr[row+1][col+1]
            bottomcenter = arr[row+1][col]

            sum_hourglass = topleft + topright + topcenter + bottomleft + bottomright + bottomcenter + core

            sums_list.append(sum_hourglass)
        
    return max(sums_list)
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
