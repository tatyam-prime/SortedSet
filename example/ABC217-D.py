# https://atcoder.jp/contests/abc217/submissions/28573630
# https://atcoder.jp/contests/abc217/submissions/28573637

# paste SortedSet here

import sys
input = sys.stdin.readline

L, Q = map(int, input().split())
s = SortedSet([0, L])
for i in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        s.add(x)
    else:
        print(s.gt(x) - s.lt(x))
        # ↓ faster
        # a = s.a
        # for i in range(len(a)):
        #     if a[i][-1] > x:
        #         j = bisect_left(a[i], x)
        #         print(a[i][j] - (a[i][j - 1] if j else a[i - 1][-1]))
        #         break
