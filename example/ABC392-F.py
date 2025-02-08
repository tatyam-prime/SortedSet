# https://atcoder.jp/contests/abc392/submissions/62566441

import sys
input = sys.stdin.readline

# paste BucketList here

N = int(input())
A = BucketList()
P = list(map(int, input().split()))

for i, p in enumerate(P):
    A.insert(p-1, i+1)

print(*A)
