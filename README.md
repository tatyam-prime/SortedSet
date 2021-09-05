# SortedSet

平方分割を利用した SortedSet です。かなり多機能です。PyPy で動きます。平衡二分木系より速いと思います。

[SortedSet](SortedSet.py)  

[使用例](example)  

## ドキュメント

## SortedSet

ソート済み列をいくつかのバケットに分割して管理します。このとき、(バケットの個数) : (バケット内の個数) = 1 : 50 くらいにします。(insert / erase の定数倍が軽く、バケット再構築の定数倍が重いため)
あるバケットが空になったり、多すぎたりしたら、1 度まとめて、均等にバケットに分割します。
基本的に、要素の変更を伴う操作は O(√N) 、伴わない操作は O(log N) と思って良いです。

### SortedSet(a=[])

iterable から SortedSet を作ります。重複がなく、かつソートされていれば O(N) 、そうでなければ O(N log N) です。

### len(s)

O(1)

### x in s / x not in s

O(log N)

### s.add(x)

x が s に含まれていなければ x を追加し、True を返します。O(√N) amotized / O(N) worst

### s.discard(x)

x が s に含まれていれば x を削除し、True を返します。O(√N) amotized / O(N) worst

### s.lt(x) / s.le(x) / s.gt(x) / s.ge(x)

x より小さい / 以下 / より大きい / 以上で 最小 / 最大 の要素を返します。存在しなければ None をを返します。O(log N)

### s[x]

下から x 番目 / 上から ~x 番目 の要素を返します。存在しない場合は IndexError を返します。O(√N) (定数倍がとても小さい)

### s.index(x)

x が何番目かを返します。存在しない場合は ValueError を返します。O(√N) (定数倍がとても小さい) + O(log N)

### s.max_right(f)

「s の要素を受け取り True / False を返す単調減少な関数」f を受け取り、f(x) = True を満たす最大の要素を返します。存在しない場合は None を返します。O(log N) × (f の計算量)

### s.min_left(f)

「s の要素を受け取り True / False を返す単調増加な関数」f を受け取り、f(x) = True を満たす最小の要素を返します。存在しない場合は None を返します。O(log N) × (f の計算量)