import pytest
import sys
import os
import random

# Add the parent directory to the path to import SortedSet
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sortedset.SortedSet import SortedSet

def test_init():
    s = SortedSet([1, 4, 3, 2, 5])
    assert list(s) == [1, 2, 3, 4, 5]
    s = SortedSet([1, 1, 2, 2, 3, 3])
    assert list(s) == [1, 2, 3]
    s = SortedSet()
    assert list(s) == []
    s = SortedSet([5, 4, 3, 2, 1])
    assert list(s) == [1, 2, 3, 4, 5]

def test_iter_reversed():
    s = SortedSet([1, 2, 3, 4, 5])
    assert list(s) == [1, 2, 3, 4, 5]
    assert list(reversed(s)) == [5, 4, 3, 2, 1]

def test_eq():
    s1 = SortedSet([1, 2, 3])
    s2 = SortedSet([3, 2, 1])
    s3 = SortedSet([1, 2, 4])
    assert s1 == s2
    assert s1 != s3
    assert s1 == [1, 2, 3]

def test_len():
    s = SortedSet([1, 2, 3, 4, 5])
    assert len(s) == 5
    s.add(6)
    assert len(s) == 6
    s.discard(1)
    assert len(s) == 5
    s.add(2) # no change
    assert len(s) == 5
    s = SortedSet()
    assert len(s) == 0

def test_repr_str():
    s = SortedSet([1, 2, 3])
    assert repr(s).startswith("SortedSet")
    assert str(s) == "{1, 2, 3}"
    s = SortedSet()
    assert str(s) == "{}"

def test_contains():
    s = SortedSet([1, 3, 5, 7, 10, 20, 30])
    assert 1 in s
    assert 2 not in s
    assert 7 in s
    assert 0 not in s
    assert 8 not in s
    assert 30 in s
    assert 31 not in s
    s = SortedSet()
    assert 1 not in s

def test_add():
    s = SortedSet()
    assert s.add(1)
    assert list(s) == [1]
    assert s.add(3)
    assert list(s) == [1, 3]
    assert s.add(2)
    assert list(s) == [1, 2, 3]
    assert not s.add(2)
    assert list(s) == [1, 2, 3]
    assert len(s) == 3

def test_discard():
    s = SortedSet([1, 2, 3, 4, 5])
    assert s.discard(3)
    assert list(s) == [1, 2, 4, 5]
    assert not s.discard(3)
    assert list(s) == [1, 2, 4, 5]
    assert s.discard(1)
    assert list(s) == [2, 4, 5]
    assert s.discard(5)
    assert list(s) == [2, 4]
    assert len(s) == 2
    s = SortedSet()
    assert not s.discard(1)

def test_lt_le_gt_ge():
    s = SortedSet([10, 20, 30, 40, 50])
    assert s.lt(30) == 20
    assert s.le(30) == 30
    assert s.gt(30) == 40
    assert s.ge(30) == 30

    assert s.lt(35) == 30
    assert s.le(35) == 30
    assert s.gt(35) == 40
    assert s.ge(35) == 40

    assert s.lt(10) is None
    assert s.le(10) == 10
    assert s.gt(50) is None
    assert s.ge(50) == 50
    
    assert s.lt(5) is None
    assert s.le(5) is None
    assert s.gt(55) is None
    assert s.ge(55) is None

def test_getitem():
    s = SortedSet([10, 20, 30, 40, 50])
    assert s[0] == 10
    assert s[2] == 30
    assert s[4] == 50
    assert s[-1] == 50
    assert s[-3] == 30
    assert s[-5] == 10
    with pytest.raises(IndexError):
        s[5]
    with pytest.raises(IndexError):
        s[-6]

def test_pop():
    s = SortedSet([10, 20, 30, 40, 50])
    assert s.pop(2) == 30
    assert list(s) == [10, 20, 40, 50]
    assert s.pop() == 50 # pop(-1)
    assert list(s) == [10, 20, 40]
    assert s.pop(0) == 10
    assert list(s) == [20, 40]
    assert len(s) == 2
    with pytest.raises(IndexError):
        s.pop(2)
    with pytest.raises(IndexError):
        s.pop(-3)

def test_index_index_right():
    s = SortedSet([10, 20, 30, 40, 50])
    assert s.index(30) == 2 # count < 30
    assert s.index_right(30) == 3 # count <= 30

    assert s.index(35) == 3
    assert s.index_right(35) == 3

    assert s.index(5) == 0
    assert s.index_right(5) == 0

    assert s.index(55) == 5
    assert s.index_right(55) == 5

def test_stress():
    s = SortedSet()
    py_s = set()
    for _ in range(1000):
        val = random.randint(0, 1000)
        if random.random() < 0.5:
            s.add(val)
            py_s.add(val)
        else:
            s.discard(val)
            if val in py_s:
                py_s.remove(val)
        assert list(s) == sorted(list(py_s))
    
    for _ in range(1000):
        if len(s) == 0: break
        idx = random.randint(0, len(s) - 1)
        val = s.pop(idx)
        py_s_list = sorted(list(py_s))
        assert val == py_s_list.pop(idx)
        py_s = set(py_s_list)
        assert list(s) == sorted(list(py_s))

def test_empty_set_operations():
    s = SortedSet()
    assert s.lt(10) is None
    assert s.le(10) is None
    assert s.gt(10) is None
    assert s.ge(10) is None
    with pytest.raises(IndexError):
        s[0]
    with pytest.raises(IndexError):
        s.pop()

def test_bucket_split():
    # Force bucket splitting by setting ratios low and adding many elements
    original_bucket_ratio = SortedSet.BUCKET_RATIO
    original_split_ratio = SortedSet.SPLIT_RATIO
    try:
        SortedSet.BUCKET_RATIO = 1
        SortedSet.SPLIT_RATIO = 4
        
        s = SortedSet()
        
        initial_elements = 10
        for i in range(initial_elements):
            s.add(i)
        
        assert list(s) == list(range(initial_elements))
        # Check number of buckets to infer if splitting happened
        # With BUCKET_RATIO=1, sqrt(10/1) ~= 3 buckets initially
        # Then adding more elements should cause splits.
        num_buckets_before = len(s.a)
        
        # Add enough elements to trigger a split
        # Each bucket holds ~3-4 elements. Adding more should split one.
        for i in range(initial_elements, initial_elements + 20):
            s.add(i)
            
        assert list(s) == list(range(initial_elements + 20))
        num_buckets_after = len(s.a)
        assert num_buckets_after > num_buckets_before
    finally:
        SortedSet.BUCKET_RATIO = original_bucket_ratio
        SortedSet.SPLIT_RATIO = original_split_ratio

def test_bucket_merge():
    # Force bucket merging by removing elements
    original_bucket_ratio = SortedSet.BUCKET_RATIO
    original_split_ratio = SortedSet.SPLIT_RATIO
    try:
        SortedSet.BUCKET_RATIO = 1
        SortedSet.SPLIT_RATIO = 4
        
        # Re-initialize to control bucket sizes
        s = SortedSet(range(100))
        
        num_buckets_before = len(s.a)
        
        # Remove elements until buckets are empty and get deleted
        for i in range(100):
            s.pop(0)
            
        assert len(s) == 0
        num_buckets_after = len(s.a)
        assert num_buckets_after < num_buckets_before
        assert num_buckets_after == 0 # Should be empty
    finally:
        SortedSet.BUCKET_RATIO = original_bucket_ratio
        SortedSet.SPLIT_RATIO = original_split_ratio

def test_large_random_ops():
    s = SortedSet()
    py_s = set()
    N = 5000
    for _ in range(N):
        op = random.randint(0, 5)
        val = random.randint(0, N)
        
        if op == 0 or op == 1: # Add
            s.add(val)
            py_s.add(val)
        elif op == 2: # Discard
            s.discard(val)
            py_s.discard(val)
        elif op == 3: # Pop
            if len(s) > 0:
                idx = random.randint(0, len(s) - 1)
                popped_s = s.pop(idx)
                py_s_list = sorted(list(py_s))
                popped_py_s = py_s_list.pop(idx)
                assert popped_s == popped_py_s
                py_s = set(py_s_list)
        elif op == 4: # Get item
             if len(s) > 0:
                idx = random.randint(0, len(s) - 1)
                assert s[idx] == sorted(list(py_s))[idx]
        elif op == 5: # Contains
            assert (val in s) == (val in py_s)

    assert list(s) == sorted(list(py_s))
