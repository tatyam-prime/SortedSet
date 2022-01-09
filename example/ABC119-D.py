# https://atcoder.jp/contests/abc119/submissions/28441723

# paste SortedSet here

import sys
input = sys.stdin.readline
INF = 1 << 60

A, B, Q = map(int, input().split())
s = SortedSet([-INF] + [int(input()) for i in range(A)] + [INF])
t = SortedSet([-INF] + [int(input()) for i in range(B)] + [INF])
for i in range(Q):
	x = int(input())
	s0 = x - s.le(x)
	s1 = s.ge(x) - x
	t0 = x - t.le(x)
	t1 = t.ge(x) - x
	print(min(max(s0, t0), max(s1, t1), s0 + t1 + min(s0, t1), s1 + t0 + min(s1, t0)))
