# https://atcoder.jp/contests/abc308/submissions/43151431

# paste SortedMultiset here

import sys
input = sys.stdin.readline

Q = int(input())
A = SortedMultiset()
X = SortedMultiset()

def add(a):
    A.add(a)
    i = A.index(a)
    l = A[i - 1] if i else None
    r = A[i + 1] if i + 1 < len(A) else None
    if l is not None and r is not None:
        X.discard(l ^ r)
    if l is not None:
        X.add(l ^ a)
    if r is not None:
        X.add(r ^ a)

def erase(a):
    i = A.index(a)
    l = A[i - 1] if i else None
    r = A[i + 1] if i + 1 < len(A) else None
    A.discard(a)
    if l is not None and r is not None:
        X.add(l ^ r)
    if l is not None:
        X.discard(l ^ a)
    if r is not None:
        X.discard(r ^ a)

for _ in range(Q):
    query = input()
    if query[0] == "3":
        print(X[0])
        continue
    t, x = query[0], int(query[2:])
    if t == '1':
        add(x)
    else:
        erase(x)
