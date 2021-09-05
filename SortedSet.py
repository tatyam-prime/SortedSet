# https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
from math import sqrt, ceil
from bisect import bisect_left, bisect_right
from typing import Iterable, TypeVar, Union
T = TypeVar('T')

class SortedSet:
	BUCKET_RATIO = 50
	REBUILD_RATIO = 170

	@classmethod
	def _new_bucket_size(cls, size: int) -> int:
		return int(ceil(sqrt(size / cls.BUCKET_RATIO)))

	def _build(self, a: list):
		size = self.size = len(a)
		bucket_size = self._new_bucket_size(self.size)
		self.a = [a[size * i // bucket_size: size *
                    (i + 1) // bucket_size] for i in range(bucket_size)]
	
	def __init__(self, a: Iterable = []):
		"Make a new SortedSet from iterable. / O(N log N)"
		self._build(sorted(set(a)))

	def __iter__(self):
		for i in self.a:
			for j in i:
				yield j
	
	def __len__(self) -> int:
		return self.size
	
	def __repr__(self) -> str:
		return str(self.a)
	
	def __str__(self) -> str:
		s = str(list(self))
		return "{" + s[1 : len(s) - 1] + "}"

	def _bucket_index(self, x: T) -> int:
		"Find the index of the bucket which should contain x. / O(log N)"
		ok = -1
		ng = len(self.a)
		a = self.a
		while ng - ok > 1:
			mid = (ng + ok) >> 1
			if a[mid][0] <= x:
				ok = mid
			else:
				ng = mid
		if ok == -1:
			return 0
		if ng == len(self.a):
			return ok
		if a[ok][-1] < x:
			return ok + (len(a[ok]) > len(a[ok + 1]))
		return ok

	def __contains__(self, x: T) -> bool:
		"O(log N)"
		if self.size == 0:
			return False
		a = self.a[self._bucket_index(x)]
		i = bisect_left(a, x)
		return i != len(a) and a[i] == x

	def add(self, x: T) -> bool:
		"Add an element and return True if added. / O(N ** 0.5)"
		if self.size == 0:
			self._build([x])
			return True
		a = self.a[self._bucket_index(x)]
		i = bisect_left(a, x)
		if i != len(a) and a[i] == x:
			return False
		a.insert(i, x)
		self.size += 1
		if len(a) > len(self.a) * self.REBUILD_RATIO:
			self._build(list(self))
		return True

	def discard(self, x: T) -> bool:
		"Remove an element and return True if removed. / O(N ** 0.5)"
		if self.size == 0:
			return False
		a = self.a[self._bucket_index(x)]
		i = bisect_left(a, x)
		if i == len(a) or a[i] != x:
			return False
		a.pop(i)
		self.size -= 1
		if len(a) == 0:
			self._build(list(self))
		return True
	
	def lt(self, x: T) -> Union[T, None]:
		"Return the largest element < x, or None if it doesn't exist. / O(log N)"
		if self.size == 0:
			return None
		i = self._bucket_index(x)
		a = self.a
		if a[i][0] >= x:
			return a[i - 1][-1] if i else None
		return a[i][bisect_left(a[i], x) - 1]

	def le(self, x: T) -> Union[T, None]:
		"Return the largest element <= x, or None if it doesn't exist. / O(log N)"
		if self.size == 0:
			return None
		i = self._bucket_index(x)
		a = self.a
		if a[i][0] > x:
			return a[i - 1][-1] if i else None
		return a[i][bisect_right(a[i], x) - 1]

	def gt(self, x: T) -> Union[T, None]:
		"Return the smallest element > x, or None if it doesn't exist. / O(log N)"
		if self.size == 0:
			return None
		i = self._bucket_index(x)
		a = self.a
		if a[i][-1] <= x:
			return a[i + 1][0] if i + 1 < len(self.a) else None
		return a[i][bisect_right(a[i], x)]

	def ge(self, x: T) -> Union[T, None]:
		"Return the smallest element >= x, or None if it doesn't exist. / O(log N)"
		if self.size == 0:
			return None
		i = self._bucket_index(x)
		a = self.a
		if a[i][-1] < x:
			return a[i + 1][0] if i + 1 < len(self.a) else None
		return a[i][bisect_left(a[i], x)]
	
	def __getitem__(self, x: int) -> T:
		"Return the x-th element, or IndexError if it doesn't exist. / O(N ** 0.5) (fast)"
		if x < 0:
			x += self.size
		if x < 0 or x >= self.size:
			raise IndexError
		for a in self.a:
			if x < len(a):
				return a[x]
			x -= len(a)
		assert False
	
	def index(self, x: T) -> int:
		"Return the index of x, or ValueError if it doesn't exist. / O(N ** 0.5) (fast)"
		if self.size == 0:
			raise ValueError
		idx = self._bucket_index(x)
		a = self.a[idx]
		i = bisect_left(a, x)
		if i == len(a) or a[i] != x:
			raise ValueError
		for j in range(idx):
			i += len(self.a[j])
		return i
