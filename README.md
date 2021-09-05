# SortedSet

平方分割を利用した SortedSet です。PyPy で動きます。平衡二分木系より速いと思います。

[SortedSet](SortedSet.py)  

[使用例](example)  

## ドキュメント

### SortedSet

ソート済み列をいくつかのバケットに分割して管理します。このとき、(バケットの個数) : (バケット内の個数) = 1 : 50 くらいにします。(insert / erase の定数倍が軽く、バケット再構築の定数倍が重いため)