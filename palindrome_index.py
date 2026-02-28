#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Write your code here
    left=0
    right=len(s)-1
    while left< right:
        mid=(left+right) // 2
        
        if s[left]==s[right]:
            right-=1
            left+=1
        else:
            if s[left+1:right+1]==s[left+1:right+1][::-1]:
                return left 
            elif s[left:right]==s[left:right][::-1]:
                return right 
            else:
                return -1 
        return -1   
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()