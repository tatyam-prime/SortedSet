# SortedSet

平衡 $\Theta(\sqrt N)$ 分木の SortedSet です。PyPy で動きます。平衡二分木系より速いと思います。

[SortedSet](sortedset/SortedSet.py)  
[SortedMultiset](sortedset/SortedMultiset.py)  
[BucketList](sortedset/BucketList.py)  
[使用例](example)  

## ドキュメント

## [SortedSet](SortedSet.py)

ソート済み列をいくつかのバケット (`list`) に分割して管理します。このとき、(バケットの個数) : (バケット内の個数) ${} = 1 : 16$ くらいにします。
あるバケットに含まれる要素が多すぎるときはそれを $2$ つのバケットに分割して、空になったときはそのバケットを削除します。  
ほとんどの操作が (要素数を $N$ として) $O(\sqrt N)$ 時間です。(定数倍軽め)  

### `SortedSet(a=[])`

iterable から SortedSet を作ります。ソートされていれば $O(N)$ 時間、ソートされていなければ $O(N \log N)$ 時間です。

### `s.a`

SortedSet の中身です。`list` の `list` になっていて、中には要素が昇順に並んでいます。各バケットには要素が存在することが保証されます。

### `len(s)`

$O(1)$ 時間

### `x in s` / `x not in s`

$O(\sqrt N)$ 時間

### `iter(s)` / `for _ in s`

要素を昇順に走査するイテレータです。走査の途中で要素の追加・削除をしてはいけません。

$O(1)$ 時間

### `reversed(s)`

要素を降順に走査するイテレータです。走査の途中で要素の追加・削除をしてはいけません。

$O(1)$ 時間

### `s.add(x)`

`x` が `s` に含まれていなければ `x` を追加し、`True` を返します。含まれている場合は `False` を返します。

償却 $O(\sqrt N)$ 時間

### `s.discard(x)`

`x` が `s` に含まれていれば `x` を削除し、`True` を返します。含まれていない場合は `False` を返します。

償却 $O(\sqrt N)$ 時間

### `s.lt(x)` / `s.le(x)` / `s.gt(x)` / `s.ge(x)`

`x` より小さい / 以下 / より大きい / 以上 で 最小 / 最大 の要素を返します。存在しなければ `None` を返します。 $O(\sqrt N)$ 時間

### `s[i]`

下から `i` 番目 / 上から `~i` 番目 の要素を返します。存在しない場合は `IndexError` を返します。  
`abs(i)` が小さいと高速に動作します。 $O(\min(|i|, \sqrt N))$ 時間

### `s.pop(i=-1)`

下から `i` 番目 / 上から `~i` 番目 の要素を削除するとともに返します。存在しない場合は `IndexError` を返します。  
`abs(i)` が小さいと高速に動作します。 $O(\min(|i|, \sqrt N))$ 時間

### `s.index(x)`

`x` より小さい要素の数を返します。`x` が `s` に含まれている場合は `list(s).index(x)` に相当します。 $O(\sqrt N)$ 時間

### `s.index_right(x)`

`x` 以下の要素の数を返します。 $O(\sqrt N)$ 時間

### `s == t`, `s != t`

集合として同一かどうかを判定します。 $O(N)$ 時間

## [SortedMultiset](SortedMultiset.py)

SortedSet の多重集合版です。同じ要素を複数入れることができます。SortedSet からの変更点は以下の通りです。

### `s.add(x)`

`x` が `s` に含まれているかどうかに関わらず `x` を追加します。償却 $O(\sqrt N)$ 時間

### `s.discard(x)`

`x` が `s` に含まれていれば `x` を **1 個** 削除し、`True` を返します。含まれていない場合は `False` を返します。

償却 $O(\sqrt N)$ 時間

(C++ の [std::multiset::erase](https://cpprefjp.github.io/reference/set/multiset/erase.html) には `x` を全て削除してしまうという罠があります。)

### `s.count(x)`

s に含まれる x の個数を返します。 $O(\sqrt N)$ 時間

## [BucketList](BucketList.py)

SortedMultiset のソートしないバージョンです。`list` と同様に扱えます。  
スライスは実装していません。

## links

コンセプトや中身の簡単な解説が書いてあります (昔は偏ったら rebuild していましたが、今は split しています)

- https://qiita.com/tatyam/items/492c70ac4c955c055602
- https://speakerdeck.com/tatyam_prime/python-dezui-qiang-falseping-heng-er-fen-tan-suo-mu-wozuo-ru
