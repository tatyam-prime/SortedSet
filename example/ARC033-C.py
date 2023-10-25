# https://atcoder.jp/contests/arc033/submissions/46930623

# paste SortedMultiset here

import sys
input = sys.stdin.readline

Q = int(input())
s = SortedMultiset()
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        s.add(x)
    else:
        x = s[x - 1]
        print(x)
        s.discard(x)
