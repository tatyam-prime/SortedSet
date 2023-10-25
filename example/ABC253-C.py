# https://atcoder.jp/contests/abc253/submissions/46930587

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
        for _ in range(c):
            if not a.discard(x):
                break
    else:
        print(a[-1] - a[0])
