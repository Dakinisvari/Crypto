def xor_upto(n):
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    else:
        return 0
n1, n2 = map(int, input().split())
xor = xor_upto(n2) ^ xor_upto(n1 - 1)
if xor % 2 == 0:
    print("even")
else:
    print("odd")
