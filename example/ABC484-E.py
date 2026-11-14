# https://atcoder.jp/contests/abc484/submissions/80863040

# paste SortedMultiset here
        
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
A = list(map(int, input().split()))
S = SortedMultiset([0])
s = 0
ans = 0
for a in A:
    s += a
    ans += S.index_right(s - L) - S.index(s - R)
    S.add(s)
print(ans)
