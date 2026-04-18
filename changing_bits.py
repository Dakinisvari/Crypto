import math
import os
import random
import re
import sys
def changeBits(a, b, queries):
    A = int(a, 2)
    B = int(b, 2)    
    ans = []
    for q in queries:
        parts = q.split()     
        if parts[0] == "set_a":
            idx = int(parts[1])
            val = int(parts[2])          
            if val == 1:
                A = A | (1 << idx)
            else:
                A = A & ~(1 << idx)       
        elif parts[0] == "set_b":
            idx = int(parts[1])
            val = int(parts[2])   
            if val == 1:
                B = B | (1 << idx)
            else:
                B = B & ~(1 << idx)
        else: 
            idx = int(parts[1])
            C = A + B
            bit = (C >> idx) & 1
            ans.append(str(bit))
    print("".join(ans))
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    ab_size = int(first_multiple_input[0])
    queries_size = int(first_multiple_input[1])
    a = input()
    b = input()
    queries = []
    for _ in range(queries_size):
        queries_item = input()
        queries.append(queries_item)
    changeBits(a, b, queries)
