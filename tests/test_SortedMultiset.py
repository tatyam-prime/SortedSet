import pytest
import sys
import os
import random

# Add the parent directory to the path to import SortedMultiset
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sortedset.SortedMultiset import SortedMultiset

def test_init():
    s = SortedMultiset([1, 4, 3, 2, 5])
    assert list(s) == [1, 2, 3, 4, 5]
    s = SortedMultiset([1, 1, 2, 2, 3, 3])
    assert list(s) == [1, 1, 2, 2, 3, 3]
    s = SortedMultiset()
    assert list(s) == []
    s = SortedMultiset([5, 4, 3, 2, 1])
    assert list(s) == [1, 2, 3, 4, 5]

def test_iter_reversed():
    s = SortedMultiset([1, 2, 2, 3, 4, 5])
    assert list(s) == [1, 2, 2, 3, 4, 5]
    assert list(reversed(s)) == [5, 4, 3, 2, 2, 1]

def test_eq():
    s1 = SortedMultiset([1, 2, 3])
    s2 = SortedMultiset([3, 2, 1])
    s3 = SortedMultiset([1, 2, 4])
    s4 = SortedMultiset([1, 2, 2, 3])
    assert s1 == s2
    assert s1 != s3
    assert s1 != s4
    assert s1 == [1, 2, 3]

def test_len():
    s = SortedMultiset([1, 2, 3, 4, 5])
    assert len(s) == 5
    s.add(6)
    assert len(s) == 6
    s.discard(1)
    assert len(s) == 5
    s.add(2) # add duplicate
    assert len(s) == 6
    s = SortedMultiset()
    assert len(s) == 0

def test_repr_str():
    s = SortedMultiset([1, 2, 2])
    assert repr(s).startswith("SortedMultiset")
    assert str(s) == "{1, 2, 2}"
    s = SortedMultiset()
    assert str(s) == "{}"

def test_contains():
    s = SortedMultiset([1, 3, 5, 5, 7, 10, 20, 30])
    assert 1 in s
    assert 2 not in s
    assert 5 in s
    assert 0 not in s
    assert 8 not in s
    assert 30 in s
    assert 31 not in s
    s = SortedMultiset()
    assert 1 not in s

def test_count():
    s = SortedMultiset([1, 2, 2, 2, 3, 3])
    assert s.count(1) == 1
    assert s.count(2) == 3
    assert s.count(3) == 2
    assert s.count(4) == 0
    s = SortedMultiset()
    assert s.count(1) == 0

def test_add():
    s = SortedMultiset()
    s.add(1)
    assert list(s) == [1]
    s.add(3)
    assert list(s) == [1, 3]
    s.add(2)
    assert list(s) == [1, 2, 3]
    s.add(2)
    assert list(s) == [1, 2, 2, 3]
    assert len(s) == 4

def test_discard():
    s = SortedMultiset([1, 2, 2, 3, 4, 5])
    assert s.discard(2)
    assert list(s) == [1, 2, 3, 4, 5]
    assert s.discard(2)
    assert list(s) == [1, 3, 4, 5]
    assert not s.discard(2)
    assert list(s) == [1, 3, 4, 5]
    assert s.discard(1)
    assert list(s) == [3, 4, 5]
    assert s.discard(5)
    assert list(s) == [3, 4]
    assert len(s) == 2
    s = SortedMultiset()
    assert not s.discard(1)

def test_lt_le_gt_ge():
    s = SortedMultiset([10, 20, 30, 30, 40, 50])
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
    s = SortedMultiset([10, 20, 30, 30, 40, 50])
    assert s[0] == 10
    assert s[2] == 30
    assert s[3] == 30
    assert s[5] == 50
    assert s[-1] == 50
    assert s[-3] == 30
    assert s[-6] == 10
    with pytest.raises(IndexError):
        s[6]
    with pytest.raises(IndexError):
        s[-7]

def test_pop():
    s = SortedMultiset([10, 20, 30, 30, 40, 50])
    assert s.pop(2) == 30
    assert list(s) == [10, 20, 30, 40, 50]
    assert s.pop() == 50 # pop(-1)
    assert list(s) == [10, 20, 30, 40]
    assert s.pop(0) == 10
    assert list(s) == [20, 30, 40]
    assert len(s) == 3
    with pytest.raises(IndexError):
        s.pop(3)
    with pytest.raises(IndexError):
        s.pop(-4)

def test_index_index_right():
    s = SortedMultiset([10, 20, 30, 30, 40, 50])
    assert s.index(30) == 2 # count < 30
    assert s.index_right(30) == 4 # count <= 30

    assert s.index(35) == 4
    assert s.index_right(35) == 4

    assert s.index(5) == 0
    assert s.index_right(5) == 0

    assert s.index(55) == 6
    assert s.index_right(55) == 6

def test_stress():
    s = SortedMultiset()
    py_s = []
    for _ in range(1000):
        val = random.randint(0, 1000)
        if random.random() < 0.5:
            s.add(val)
            py_s.append(val)
        else:
            if s.discard(val):
                py_s.remove(val)
        py_s.sort()
        assert list(s) == py_s
    
    for _ in range(1000):
        if len(s) == 0: break
        idx = random.randint(0, len(s) - 1)
        val = s.pop(idx)
        assert val == py_s.pop(idx)
        assert list(s) == py_s

def test_empty_set_operations():
    s = SortedMultiset()
    assert s.lt(10) is None
    assert s.le(10) is None
    assert s.gt(10) is None
    assert s.ge(10) is None
    with pytest.raises(IndexError):
        s[0]
    with pytest.raises(IndexError):
        s.pop()

def test_bucket_split():
    original_bucket_ratio = SortedMultiset.BUCKET_RATIO
    original_split_ratio = SortedMultiset.SPLIT_RATIO
    try:
        SortedMultiset.BUCKET_RATIO = 1
        SortedMultiset.SPLIT_RATIO = 4
        
        s = SortedMultiset()
        
        initial_elements = 10
        for i in range(initial_elements):
            s.add(i)
        
        assert list(s) == list(range(initial_elements))
        num_buckets_before = len(s.a)
        
        for i in range(initial_elements, initial_elements + 20):
            s.add(i)
            
        assert list(s) == list(range(initial_elements + 20))
        num_buckets_after = len(s.a)
        assert num_buckets_after > num_buckets_before
    finally:
        SortedMultiset.BUCKET_RATIO = original_bucket_ratio
        SortedMultiset.SPLIT_RATIO = original_split_ratio

def test_bucket_merge():
    original_bucket_ratio = SortedMultiset.BUCKET_RATIO
    original_split_ratio = SortedMultiset.SPLIT_RATIO
    try:
        SortedMultiset.BUCKET_RATIO = 1
        SortedMultiset.SPLIT_RATIO = 4
        
        s = SortedMultiset(range(100))
        
        num_buckets_before = len(s.a)
        
        for _ in range(100):
            s.pop(0)
            
        assert len(s) == 0
        num_buckets_after = len(s.a)
        assert num_buckets_after < num_buckets_before
        assert num_buckets_after == 0
    finally:
        SortedMultiset.BUCKET_RATIO = original_bucket_ratio
        SortedMultiset.SPLIT_RATIO = original_split_ratio

def test_large_random_ops():
    s = SortedMultiset()
    py_s = []
    N = 5000
    for _ in range(N):
        op = random.randint(0, 6)
        val = random.randint(0, N)
        
        if op == 0 or op == 1: # Add
            s.add(val)
            py_s.append(val)
        elif op == 2: # Discard
            if s.discard(val):
                py_s.remove(val)
        elif op == 3: # Pop
            if len(s) > 0:
                py_s.sort()
                idx = random.randint(0, len(s) - 1)
                popped_s = s.pop(idx)
                popped_py_s = py_s.pop(idx)
                assert popped_s == popped_py_s
        elif op == 4: # Get item
             if len(s) > 0:
                py_s.sort()
                idx = random.randint(0, len(s) - 1)
                assert s[idx] == py_s[idx]
        elif op == 5: # Contains
            assert (val in s) == (val in py_s)
        elif op == 6: # Count
            py_s.sort()
            assert s.count(val) == py_s.count(val)

    py_s.sort()
    assert list(s) == py_s
