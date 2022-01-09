# https://atcoder.jp/contests/abc140/submissions/28441915

# paste SortedMultiset here

import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
Q = [0] * N
for i in range(N):
    Q[P[i] - 1] = i

s = SortedMultiset([-1, -1, N, N])
ans = 0
cnt = 0
for x in reversed(Q):
    s.add(x)
    i = s.index(x)
    v = s[i - 2]
    w = s[i - 1]
    y = s[i + 1]
    z = s[i + 2]
    cnt += (z - y) * (x - w) + (y - x) * (w - v)
    ans += cnt

print(ans)
