import math
import os
import random
import re
import sys
def cipher(k, s):
    n = len(s) - k + 1 
    res = [0] * n  
    curr_xor = 0   
    for i in range(n):
        res[i] = int(s[i]) ^ curr_xor
        curr_xor ^= res[i]
        if i >= k - 1:
            curr_xor ^= res[i - (k - 1)]
    return ''.join(map(str, res))    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = input()
    result = cipher(k, s)
    fptr.write(result + '\n')
    fptr.close()
