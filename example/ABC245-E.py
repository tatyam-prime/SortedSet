# https://atcoder.jp/contests/abc245/submissions/30714614

# paste SortedMultiset here

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

A = [A[i] << 30 | B[i] for i in range(N)]
C = [C[i] << 30 | D[i] for i in range(M)]
A.sort(reverse=True)
C.sort()
C.insert(0, 0)

s = SortedMultiset()
MASK = (1 << 30) - 1

for xy in A:
    while C[-1] >= xy:
        s.add(C.pop() & MASK)
    a = s.ge(xy & MASK)
    if a is None:
        exit(print("No"))
    s.discard(a)

print("Yes")
