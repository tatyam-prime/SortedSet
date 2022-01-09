# https://atcoder.jp/contests/abc228/submissions/28441686

# paste SortedSet here

import sys
input = sys.stdin.readline

N = 1 << 20
A = [-1] * N
Q = int(input())
mask = N - 1
s = SortedSet(range(N))

for i in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        y = s.ge(x & mask)
        if y is None:
            y = s[0]
        A[y] = x
        s.discard(y)
    else:
        print(A[x & mask])
