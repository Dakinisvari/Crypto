import math
import os
import random
import re
import sys
def solve(a):   
    n = len(a)
    b = [0] * (n + 1)
    b[0] = a[0]
    for i in range(1, n):
        b[i] = (a[i-1] * a[i]) // math.gcd(a[i-1], a[i])
    b[n] = a[n-1]
    return b
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        a_count = int(input().strip())
        a = list(map(int, input().rstrip().split()))
        result = solve(a)
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
    fptr.close()
