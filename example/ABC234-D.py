# https://atcoder.jp/contests/abc234/submissions/28441677

# paste SortedSet here

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
P = list(map(int, input().split()))
K -= 1
s = SortedSet(P[:K])

for i in range(K, N):
    s.add(P[i])
    print(s[~K])
