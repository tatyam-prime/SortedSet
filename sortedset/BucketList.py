# https://github.com/tatyam-prime/SortedSet/blob/main/sortedset/BucketList.py
import math
from typing import Generic, Iterable, Iterator, TypeVar
T = TypeVar('T')

class BucketList(Generic[T]):
    BUCKET_RATIO = 16
    SPLIT_RATIO = 24
    
    def __init__(self, a: Iterable[T] = []) -> None:
        a = list(a)
        n = self.size = len(a)
        num_bucket = int(math.ceil(math.sqrt(n / self.BUCKET_RATIO)))
        self.a = [a[n * i // num_bucket : n * (i + 1) // num_bucket] for i in range(num_bucket)]

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i: yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i): yield j
    
    def __eq__(self, other) -> bool:
        if len(self) != len(other): return False
        for x, y in zip(self, other):
            if x != y: return False
        return True
    
    def __len__(self) -> int:
        return self.size
    
    def __repr__(self) -> str:
        return "BucketList" + str(self.a)
    
    def __str__(self) -> str:
        return str(list(self))

    def __contains__(self, x: T) -> bool:
        "Return True if x is in the bucket list. / O(N)"
        for y in self:
            if x == y: return True
        return False
    
    def _insert(self, a: list[T], b: int, i: int, x: T) -> None:
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.SPLIT_RATIO:
            mid = len(a) >> 1
            self.a[b:b+1] = [a[:mid], a[mid:]]

    def insert(self, i: int, x: T) -> None:
        "Insert x at the i-th position. / O(√N)"
        if self.size == 0:
            if i != 0 and i != -1: raise IndexError
            self.a = [[x]]
            self.size = 1
            return
        if i < 0:
            for b, a in enumerate(reversed(self.a)):
                i += len(a)
                if i >= 0: return self._insert(a, len(self.a) + ~b, i, x)
        else:
            for b, a in enumerate(self.a):
                if i <= len(a): return self._insert(a, b, i, x)
                i -= len(a)
        raise IndexError

    def append(self, x: T) -> None:
        "Append x to the end of the list. / amortized O(1)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return
        a = self.a[-1]
        return self._insert(a, len(self.a) - 1, len(a), x)
    
    def extend(self, a: Iterable[T]) -> None:
        for x in a: self.append(x)
    
    def __getitem__(self, i: int) -> T:
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0: return a[i]
        else:
            for a in self.a:
                if i < len(a): return a[i]
                i -= len(a)
        raise IndexError
    
    def _pop(self, a: list[T], b: int, i: int) -> T:
        ans = a.pop(i)
        self.size -= 1
        if not a: del self.a[b]
        return ans
    
    def pop(self, i: int = -1) -> T:
        "Remove and return the i-th element. / O(√N) / O(-i) if i < 0"
        if i < 0:
            for b, a in enumerate(reversed(self.a)):
                i += len(a)
                if i >= 0: return self._pop(a, ~b, i)
        else:
            for b, a in enumerate(self.a):
                if i < len(a): return self._pop(a, b, i)
                i -= len(a)
        raise IndexError

    def count(self, x: T) -> int:
        "Return the number of occurrences of x. / O(N)"
        return sum(1 for y in self if x == y)

    def index(self, x: T) -> int:
        "Return the index of the first occurrence of x, raise ValueError if not found. / O(N)"
        for i, y in enumerate(self):
            if x == y: return i
        raise ValueError
    
    def remove(self, x: T) -> None:
        "Remove the first occurrence of x, raise ValueError if not found. / O(N)"
        self.pop(self.index(x))

    def clear(self) -> None:
        self.a = []
        self.size = 0

    def reverse(self) -> None:
        self.a.reverse()
        for a in self.a: a.reverse()

    def copy(self) -> 'BucketList[T]':
        return BucketList(self)
