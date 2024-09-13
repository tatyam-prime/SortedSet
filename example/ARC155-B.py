# https://atcoder.jp/contests/arc155/submissions/38361198

import sys
input = sys.stdin.readline

# paste SortedSet here

INF = 1 << 60
s = SortedSet([-INF, INF])
def add(a, b):
    s.add(a + b)
    s.add(a - b)

Q, A, B = map(int, input().split())
add(A, B)

for _ in range(Q):
    t, a, b = map(int, input().split())
    if t == 1:
        add(a, b)
    else:
        print(max(0, min(s.ge(a) - b, a - s.le(b))))
