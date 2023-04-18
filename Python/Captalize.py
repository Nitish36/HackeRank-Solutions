#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    x = len(s)
    new_str = s[0].upper()+s[1:x]
    
    for i in range(len(new_str)):
        if new_str[i] == ' ':
            new_str=new_str[0:i+1]+new_str[i+1].upper()+new_str[i+2:]
    
    return new_str
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
