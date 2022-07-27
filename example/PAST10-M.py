# https://atcoder.jp/contests/past202203-open/submissions/33549843

# paste SortedSet here

import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
P = list(map(int, input().split()))

rank = SortedSet(P[i] << 20 | i for i in range(N))

for _ in range(Q):
    query = input()
    t = query[0]
    query = query[2:]
    if t == '1':
        i, x = map(int, query.split())
        i -= 1
        rank.discard(P[i] << 20 | i)
        P[i] = x
        rank.add(x << 20 | i)
    elif t == '2':
        i = int(query)
        i -= 1
        print(N - rank.index(P[i] << 20))
    else:
        r = int(query)
        print((rank[-r] & 0xfffff) + 1)
