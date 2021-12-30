# https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py
import math
from bisect import bisect_left, bisect_right, insort
from typing import Iterable, Iterator, TypeVar, Union, Generic
T = TypeVar('T')

class SortedMultiset(Generic[T]):
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    @classmethod
    def _new_bucket_size(cls, size: int) -> int:
        return int(math.ceil(math.sqrt(size / cls.BUCKET_RATIO)))

    def _build(self, *a) -> None:
        a = a[0] if a else list(self)
        size = self.size = len(a)
        bucket_size = self._new_bucket_size(self.size)
        self.a = [a[size * i // bucket_size : size * (i + 1) // bucket_size] for i in range(bucket_size)]
    
    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)"
        a = list(a)
        if not all(a[i] <= a[i + 1] for i in range(len(a) - 1)):
            a = sorted(a)
        self._build(a)

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i: yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i): yield j
    
    def __len__(self) -> int:
        return self.size
    
    def __repr__(self) -> str:
        return "SortedMultiset" + str(self.a)
    
    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _bucket_index(self, x: T) -> int:
        "Find the rightmost index of the bucket which should contain x. self must not be empty. / O(log N)"
        ok = 0
        ng = len(self.a)
        a = self.a
        while ng - ok > 1:
            mid = (ng + ok) >> 1
            if a[mid][0] <= x: ok = mid
            else: ng = mid
        return ok

    def _bucket_index_left(self, x: T) -> int:
        "Find the leftmost index of the bucket which should contain x. self must not be empty. / O(log N)"
        ok = len(self.a) - 1
        ng = -1
        a = self.a
        while ok - ng > 1:
            mid = (ng + ok) >> 1
            if a[mid][-1] >= x:
                ok = mid
            else:
                ng = mid
        return ok

    def __contains__(self, x: T) -> bool:
        "O(log N)"
        if self.size == 0: return False
        a = self.a[self._bucket_index(x)]
        i = bisect_left(a, x)
        return i != len(a) and a[i] == x

    def count(self, x: T) -> int:
        "Count the number of x. / O(√N) (fast)"
        if self.size == 0:
            return 0
        i = self._bucket_index(x)
        a = self.a
        ans = bisect_right(a[i], x)
        while i and a[i][0] == x:
            i -= 1
            ans += len(a[i])
        ans -= bisect_left(a[i], x)
        return ans

    def add(self, x: T) -> None:
        "Add an element. / O(√N)"
        if self.size == 0:
            self._build([x])
            return
        a = self.a[self._bucket_index(x)]
        insort(a, x)
        self.size += 1
        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0: return False
        a = self.a[self._bucket_index(x)]
        i = bisect_left(a, x)
        if i == len(a) or a[i] != x: return False
        a.pop(i)
        self.size -= 1
        if len(a) == 0: self._build()
        return True
    
    def lt(self, x: T) -> Union[T, None]:
        "Return the largest element < x, or None if it doesn't exist. / O(log N)"
        if self.size == 0: return
        i = self._bucket_index_left(x)
        a = self.a
        if a[i][0] >= x:
            return a[i - 1][-1] if i else None
        return a[i][bisect_left(a[i], x) - 1]

    def le(self, x: T) -> Union[T, None]:
        "Return the largest element <= x, or None if it doesn't exist. / O(log N)"
        if self.size == 0: return
        i = self._bucket_index_left(x)
        a = self.a
        if a[i][0] > x:
            return a[i - 1][-1] if i else None
        return a[i][bisect_right(a[i], x) - 1]

    def gt(self, x: T) -> Union[T, None]:
        "Return the smallest element > x, or None if it doesn't exist. / O(log N)"
        if self.size == 0: return
        i = self._bucket_index(x)
        a = self.a
        if a[i][-1] <= x:
            return a[i + 1][0] if i + 1 < len(self.a) else None
        return a[i][bisect_right(a[i], x)]

    def ge(self, x: T) -> Union[T, None]:
        "Return the smallest element >= x, or None if it doesn't exist. / O(log N)"
        if self.size == 0: return
        i = self._bucket_index(x)
        a = self.a
        if a[i][-1] < x:
            return a[i + 1][0] if i + 1 < len(self.a) else None
        return a[i][bisect_left(a[i], x)]
    
    def __getitem__(self, x: int) -> T:
        "Return the x-th element, or IndexError if it doesn't exist. / O(√N) (fast)"
        if x < 0: x += self.size
        if x < 0 or x >= self.size: raise IndexError
        for a in self.a:
            if x < len(a): return a[x]
            x -= len(a)
        assert False  # unreachable
    
    def index(self, x: T) -> int:
        "Return the number of elements < x. / O(√N) (fast)"
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Return the number of elements <= x. / O(√N) (fast)"
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans
