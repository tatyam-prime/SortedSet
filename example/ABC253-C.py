# https://atcoder.jp/contests/abc253/submissions/32059406

# paste SortedMultiset here

import sys
input = sys.stdin.readline

Q = int(input())
a = SortedMultiset()
for i in range(Q):
    query = input()
    if query[0] == "1":
        x = int(query[2:])
        a.add(x)
    elif query[0] == "2":
        x, c = map(int, query[2:].split())
        c = min(c, a.count(x))
        for _ in range(c):
            a.discard(x)
    else:
        print(a[-1] - a[0])
