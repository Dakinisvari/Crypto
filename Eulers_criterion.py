import math
import os
import random
import re
import sys
def solve(a, m):
    a = a % m
    if a == 0:
        return "YES"
    res = pow(a, (m - 1) // 2, m)
    if res == 1:
        return "YES"
    else:
        return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        a = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        result = solve(a, m)
        fptr.write(result + '\n')
    fptr.close()
