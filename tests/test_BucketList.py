import pytest
import sys
import os
import random

# Add the parent directory to the path to import BucketList
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sortedset.BucketList import BucketList

def test_init():
    bl = BucketList([1, 2, 3, 4, 5])
    assert list(bl) == [1, 2, 3, 4, 5]
    bl = BucketList("hello")
    assert list(bl) == ['h', 'e', 'l', 'l', 'o']
    bl = BucketList()
    assert list(bl) == []

def test_iter_reversed():
    data = [1, 2, 3, 4, 5]
    bl = BucketList(data)
    assert list(bl) == data
    assert list(reversed(bl)) == list(reversed(data))

def test_eq():
    bl1 = BucketList([1, 2, 3])
    bl2 = BucketList([1, 2, 3])
    bl3 = BucketList([1, 2, 4])
    l1 = [1, 2, 3]
    assert bl1 == bl2
    assert bl1 != bl3
    assert bl1 == l1

def test_len():
    data = [1, 2, 3, 4, 5]
    bl = BucketList(data)
    assert len(bl) == 5
    bl.append(6)
    assert len(bl) == 6
    bl.pop()
    assert len(bl) == 5
    bl.clear()
    assert len(bl) == 0

def test_repr_str():
    bl = BucketList([1, 2, 3])
    assert repr(bl).startswith("BucketList")
    assert str(bl) == "[1, 2, 3]"
    bl = BucketList()
    assert str(bl) == "[]"

def test_contains():
    bl = BucketList([1, 3, 5, 7, 10, 20, 30])
    assert 1 in bl
    assert 2 not in bl
    assert 30 in bl
    assert 31 not in bl
    bl = BucketList()
    assert 1 not in bl

def test_insert():
    bl = BucketList()
    bl.insert(0, 10)
    assert list(bl) == [10]
    bl.insert(0, 5)
    assert list(bl) == [5, 10]
    bl.insert(1, 7)
    assert list(bl) == [5, 7, 10]
    bl.insert(3, 12)
    assert list(bl) == [5, 7, 10, 12]
    bl.insert(-1, 11)
    assert list(bl) == [5, 7, 10, 11, 12]
    with pytest.raises(IndexError):
        bl.insert(100, 1)
    with pytest.raises(IndexError):
        bl.insert(-100, 1)

def test_append_extend():
    bl = BucketList()
    bl.append(1)
    assert list(bl) == [1]
    bl.append(2)
    assert list(bl) == [1, 2]
    bl.extend([3, 4, 5])
    assert list(bl) == [1, 2, 3, 4, 5]
    bl.extend([])
    assert list(bl) == [1, 2, 3, 4, 5]

def test_getitem():
    bl = BucketList([10, 20, 30, 40, 50])
    assert bl[0] == 10
    assert bl[2] == 30
    assert bl[4] == 50
    assert bl[-1] == 50
    assert bl[-3] == 30
    assert bl[-5] == 10
    with pytest.raises(IndexError):
        bl[5]
    with pytest.raises(IndexError):
        bl[-6]

def test_pop():
    bl = BucketList([10, 20, 30, 40, 50])
    assert bl.pop(2) == 30
    assert list(bl) == [10, 20, 40, 50]
    assert bl.pop() == 50
    assert list(bl) == [10, 20, 40]
    assert bl.pop(0) == 10
    assert list(bl) == [20, 40]
    assert len(bl) == 2
    with pytest.raises(IndexError):
        bl.pop(2)
    with pytest.raises(IndexError):
        bl.pop(-3)

def test_count():
    bl = BucketList([1, 2, 2, 3, 2, 4])
    assert bl.count(1) == 1
    assert bl.count(2) == 3
    assert bl.count(5) == 0

def test_index():
    bl = BucketList([1, 2, 3, 2, 1])
    assert bl.index(1) == 0
    assert bl.index(2) == 1
    assert bl.index(3) == 2
    with pytest.raises(ValueError):
        bl.index(4)

def test_remove():
    bl = BucketList([1, 2, 3, 2, 1])
    bl.remove(2)
    assert list(bl) == [1, 3, 2, 1]
    bl.remove(1)
    assert list(bl) == [3, 2, 1]
    with pytest.raises(ValueError):
        bl.remove(4)

def test_clear():
    bl = BucketList([1, 2, 3])
    bl.clear()
    assert len(bl) == 0
    assert list(bl) == []
    assert bl.a == []

def test_reverse():
    data = [1, 2, 3, 4, 5, 6]
    bl = BucketList(data)
    bl.reverse()
    data.reverse()
    assert list(bl) == data
    bl.reverse()
    data.reverse()
    assert list(bl) == data

def test_copy():
    bl1 = BucketList([1, 2, 3])
    bl2 = bl1.copy()
    assert bl1 == bl2
    assert bl1 is not bl2
    bl2.append(4)
    assert list(bl1) == [1, 2, 3]
    assert list(bl2) == [1, 2, 3, 4]

def test_empty_list_operations():
    bl = BucketList()
    with pytest.raises(IndexError):
        bl[0]
    with pytest.raises(IndexError):
        bl.pop()
    with pytest.raises(ValueError):
        bl.index(1)
    with pytest.raises(ValueError):
        bl.remove(1)
    assert bl.count(1) == 0
    assert (1 in bl) is False

def test_bucket_split_and_merge():
    original_bucket_ratio = BucketList.BUCKET_RATIO
    original_split_ratio = BucketList.SPLIT_RATIO
    try:
        BucketList.BUCKET_RATIO = 1
        BucketList.SPLIT_RATIO = 4
        
        bl = BucketList()
        
        # Test split
        num_buckets_before = len(bl.a)
        for i in range(30):
            bl.append(i)
        num_buckets_after = len(bl.a)
        assert num_buckets_after > num_buckets_before
        assert list(bl) == list(range(30))

        # Test merge
        num_buckets_before = len(bl.a)
        for _ in range(30):
            bl.pop()
        num_buckets_after = len(bl.a)
        assert num_buckets_after < num_buckets_before
        assert len(bl) == 0
        assert num_buckets_after == 0

    finally:
        BucketList.BUCKET_RATIO = original_bucket_ratio
        BucketList.SPLIT_RATIO = original_split_ratio

def test_large_random_ops():
    bl = BucketList()
    py_l = []
    N = 2000
    for _ in range(N):
        op = random.randint(0, 8)
        
        if op == 0: # append
            val = random.randint(0, N)
            bl.append(val)
            py_l.append(val)
        elif op == 1: # insert
            val = random.randint(0, N)
            idx = random.randint(0, len(py_l))
            bl.insert(idx, val)
            py_l.insert(idx, val)
        elif op == 2: # pop
            if py_l:
                idx = random.randint(0, len(py_l) - 1)
                assert bl.pop(idx) == py_l.pop(idx)
        elif op == 3: # getitem
             if py_l:
                idx = random.randint(0, len(py_l) - 1)
                assert bl[idx] == py_l[idx]
        elif op == 4: # contains
            val = random.randint(0, N)
            assert (val in bl) == (val in py_l)
        elif op == 5: # count
            val = random.randint(0, N)
            assert bl.count(val) == py_l.count(val)
        elif op == 6: # remove
            if py_l:
                val = random.choice(py_l)
                bl.remove(val)
                py_l.remove(val)
        elif op == 7: # index
            if py_l:
                val = random.choice(py_l)
                assert bl.index(val) == py_l.index(val)
        elif op == 8: # reverse
            bl.reverse()
            py_l.reverse()

    assert list(bl) == py_l
