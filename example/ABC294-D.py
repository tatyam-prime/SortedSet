# https://atcoder.jp/contests/abc294/submissions/41999391

# paste SortedMultiset here

import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
que = SortedSet()

n = 1
for _ in range(Q):
    query = input()
    type = query[0]
    if type == '1':
        que.add(n)
        n += 1
    elif type == '2':
        x = int(query[2:])
        que.discard(x)
    else:
        print(que[0])
