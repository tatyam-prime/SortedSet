# https://atcoder.jp/contests/past202112-open/submissions/28629435

# paste SortedSet here

import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
S = input().split()
S = SortedSet((S[i], i) for i in range(N))
for i in range(Q):
    X, T = input().split()
    X = S[int(X) - 1]
    S.discard(X)
    S.add((T, X[1]))

ans = [""] * N
for name, id in S:
    ans[id] = name
for i in ans:
    print(i)
