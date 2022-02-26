# https://atcoder.jp/contests/abc241/submissions/29717385

# paste SortedMultiset here

import sys
input = sys.stdin.readline

Q = int(input())
A = SortedMultiset()
for _ in range(Q):
    s = input()
    if s[0] == "1":
        x = int(s[2:])
        A.add(x)
    elif s[0] == "2":
        x, k = map(int, s[2:].split())
        i = A.index_right(x) - k
        print(-1 if i < 0 else A[i])
    else:
        x, k = map(int, s[2:].split())
        i = A.index(x) + k - 1
        print(-1 if i >= len(A) else A[i])
