# https://atcoder.jp/contests/abc281/submissions/42037264

# paste SortedMultiset here

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
first = sorted(A[:M])
low = SortedMultiset(first[:K])
high = SortedMultiset(first[K:])
ans = sum(first[:K])
print(ans)

for i in range(M, N):
    x = A[i]
    if x < low[-1]:
        ans -= low[-1]
        high.add(low.pop(-1))
        ans += x
        low.add(x)
    else:
        high.add(x)
    x = A[i - M]
    if x < high[0]:
        ans -= x
        low.discard(x)
        ans += high[0]
        low.add(high.pop(0))
    else:
        high.discard(x)
    print(ans)
