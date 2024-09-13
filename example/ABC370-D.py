# https://atcoder.jp/contests/abc370/submissions/57703551

# paste SortedSet here

import sys
input = sys.stdin.readline

H, W, Q = map(int, input().split())
rows = [SortedSet(range(W)) for _ in range(H)]
cols = [SortedSet(range(H)) for _ in range(W)]
ans = H * W

def remove(x, y):
    if x is None or y is None: return
    rows[x].discard(y)
    cols[y].discard(x)
    global ans
    ans -= 1
    
for _ in range(Q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if y in rows[x]:
        remove(x, y)
    else:
        remove(x, rows[x].lt(y))
        remove(x, rows[x].gt(y))
        remove(cols[y].lt(x), y)
        remove(cols[y].gt(x), y)

print(ans)
