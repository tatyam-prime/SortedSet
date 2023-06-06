# SortedSet

平衡 $\Theta(\sqrt N)$ 分木の SortedSet です。PyPy で動きます。平衡二分木系より速いと思います。

[SortedSet](SortedSet.py)  
[SortedMultiset](SortedMultiset.py)  
[使用例](example)  

## ドキュメント

## [SortedSet](SortedSet.py)

ソート済み列をいくつかのバケット (`list`) に分割して管理します。このとき、(バケットの個数) : (バケット内の個数) ${} = 1 : 50$ くらいにします。(`list` の `insert` / `pop` の定数倍が軽く、バケット再構築の定数倍が重いため)  
あるバケットが空になったり、多すぎたりしたら、1 度まとめて、均等にバケットに分割します。  
基本的に、全ての操作が (要素数を $N$ として) $O(\sqrt N)$ 時間で、(どのバケットか探す時間) < (バケットの中を探す時間) < (バケットへの挿入・削除) の順に重くなります。

### `SortedSet(a=[])`

iterable から SortedSet を作ります。重複がなく、かつソートされていれば $O(N)$ 時間、そうでなければ $O(N \log N)$ 時間です。

### `s.a`

SortedSet の中身です。`list` の `list` になっていて、中には要素が昇順に並んでいます。各バケットには要素が存在することが保証されます。

### `len(s)`

$O(1)$ 時間

### `x in s` / `x not in s`

$O(\sqrt N)$ 時間

### `iter(s)` / `for _ in s`

要素を昇順に走査するイテレータです。走査の途中で要素の追加 / 削除をしてはいけません。

$O(1)$ 時間

### `reversed(s)`

要素を降順に走査するイテレータです。走査の途中で要素の追加 / 削除をしてはいけません。

$O(1)$ 時間

### `s.add(x)`

`x` が `s` に含まれていなければ `x` を追加し、`True` を返します。含まれている場合は `False` を返します。

償却 $O(\sqrt N)$ 時間

### `s.discard(x)`

`x` が `s` に含まれていれば `x` を削除し、`True` を返します。含まれていない場合は `False` を返します。

償却 $O(\sqrt N)$ 時間

### `s.lt(x)` / `s.le(x)` / `s.gt(x)` / `s.ge(x)`

`x` より小さい / 以下 / より大きい / 以上 で 最小 / 最大 の要素を返します。存在しなければ `None` を返します。 $O(\sqrt N)$ 時間

### `s[x]`

下から `x` 番目 / 上から `~x` 番目 の要素を返します。存在しない場合は `IndexError` を返します。  
`abs(x)` が小さいと高速に動作します。 $O(\frac{|x|}{\sqrt N})$ 時間

### `s.index(x)`

`x` より小さい要素の数を返します。`x` が `s` に含まれている場合は `list(s).index(x)` に相当します。 $O(\sqrt N)$ 時間

### `s.index_right(x)`

`x` 以下の要素の数を返します。 $O(\sqrt N)$ 時間

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

## links

コンセプトや中身の簡単な解説が書いてあります

- https://qiita.com/tatyam/items/492c70ac4c955c055602
- https://speakerdeck.com/tatyam_prime/python-dezui-qiang-falseping-heng-er-fen-tan-suo-mu-wozuo-ru
