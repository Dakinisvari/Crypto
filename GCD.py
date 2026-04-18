import math
if __name__ == '__main__':
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    g = A[0]
    for x in A:
        g = math.gcd(g, x)
    if g == 1:
        print(0)
    else:
        ans = 0
        i = 1
        while i * i <= g:
            if g % i == 0:
                if i > 1:
                    val = (k // i) * i
                    if val > ans:
                        ans = val
                d = g // i
                if d > 1:
                    val = (k // d) * d
                    if val > ans:
                        ans = val
            i += 1
        print(ans)
