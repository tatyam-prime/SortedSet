# SortedSet

平方分割を利用した SortedSet です。PyPy で動きます。平衡二分木系より速いと思います。

[SortedSet](SortedSet.py)  
[SortedMultiset](SortedMultiset.py)  
[使用例](example)  

## ドキュメント

## [SortedSet](SortedSet.py)

ソート済み列をいくつかのバケット (list) に分割して管理します。このとき、(バケットの個数) : (バケット内の個数) = 1 : 50 くらいにします。(list の insert / pop の定数倍が軽く、バケット再構築の定数倍が重いため)  
あるバケットが空になったり、多すぎたりしたら、1 度まとめて、均等にバケットに分割します。  
基本的に、全ての操作が O(√N) で、(どのバケットか探す時間) < (バケットの中を探す時間) < (バケットへの挿入・削除) の順に重くなります。

### SortedSet(a=[])

iterable から SortedSet を作ります。重複がなく、かつソートされていれば O(N) 、そうでなければ O(N log N) です。

### s.a

SortedSet の中身です。list の list になっていて、中には要素が昇順に並んでいます。各バケットには要素が存在することが保証されます。

### len(s)

O(1)

### x in s / x not in s

O(√N)

### s.add(x)

x が s に含まれていなければ x を追加し、True を返します。O(√N) amotized / O(N) worst

### s.discard(x)

x が s に含まれていれば x を削除し、True を返します。O(√N) amotized / O(N) worst

### s.lt(x) / s.le(x) / s.gt(x) / s.ge(x)

x より小さい / 以下 / より大きい / 以上で 最小 / 最大 の要素を返します。存在しなければ None をを返します。O(√N)

### s[x]

下から x 番目 / 上から ~x 番目 の要素を返します。存在しない場合は IndexError を返します。O(√N) (定数倍が小さい)

### s.index(x)

x より小さい要素の数を返します。x が s に含まれている場合は list(s).index(x) に相当します。O(√N) (定数倍が小さい)

### s.index_right(x)

x 以下の要素の数を返します。O(√N) (定数倍が小さい)

## [SortedMultiset](SortedMultiset.py)

SortedSet の多重集合版です。同じ要素を複数入れることができます。SortedSet からの変更点は以下の通りです。

### s.add(x)

x が s に含まれているかどうかに関わらず x を追加します。何も返しません。O(√N) amotized / O(N) worst

### s.discard(x)

x が s に含まれていれば x を **1 個** 削除し、True を返します。O(√N) amotized / O(N) worst  
(C++ の [std::multiset::erase](https://cpprefjp.github.io/reference/set/multiset/erase.html) には x を全て削除してしまうという罠があります。)

### s.count(x)

s に含まれる x の個数を返します。O(√N) (定数倍が小さい)
