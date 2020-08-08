"""
セットとは
セット（Set）というデータ型は、複数のデータを持つデータ型の一つで、
集合を表現することができます。1つのセットの中に同じ値は1つのみ登録可能で、
重複のないデータ型としても重宝される代物です（リストについでよく利用します）。

セットの作成
セットは幾つかの方法で作ることができます。具体的には以下のように実装します。
"""

# 空のセットを作る
empty_set = set()
print(empty_set)    # set()

# 初期値を与えて、セットを作成する
even_numbers = {0, 2, 4, 6, 8}
print(even_numbers)    # {8, 0, 2, 4, 6}

# 文字列から生成する
set_ = set('letters')
print(set_)    # {'s', 'l', 't', 'r', 'e'}

# リストから作る
set_ = set([1, 2, 3, 4, 5])
print(set_)    # {1, 2, 3, 4, 5}

# タプルから作る
set_ = set(("aaa", "bbb", "ccc"))
print(set_)    # {'ccc', 'aaa', 'bbb'}

# 辞書（Dictionary）から作る
# 辞書のキーのみが使われます
set_ = set({"key1":"value1", "key2":"value2"})
print(set_)    # {'key1', 'key2'}


"""
ただ、1点だけ注意が必要で、空のセットを作る場合に、以下のように行うと、
意図せず辞書型になってしまいます。
"""

# 注意：{}で空セットを作れそうだが、実際には空の辞書が作られる
set_ = {}
print(set_)    # {} : これはセットではない！！

"""
辞書と同じく同じ波かっこ（{}）を使うので、少しだけ混乱するかもしれませんが、
慣れるとどうってないことです。
"""

# セットの参照
#  セット内のデータ参照には、for文などの構文を利用します。

set_ = set("abc")
for s in set_:
    print(s) # 出てくる順序は追加順とは限らない
# c
# a
# b

"""
セットは中身を順序立てて持たない（リストではない）ので、
以下のようなインデックス参照はできません。
"""

set_ = set("abc")
set_[0] # エラー
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'set' object does not support indexing

# inを使った存在確認
# セットを使う理由の一つに、「inを使った存在確認がリストに比べて非常に高速だ」という点があります。
# 使い方は以下の通りです。

# inを使った存在確認

numbers = {1, 2, 3}

# 存在するキーの場合
print(1 in numbers) # True

# 存在しないキーの場合
print(4 in numbers) # False

"""
使い方はリストと同じですね。これは非常に便利なので、是非是非使えるようになりたいところです。
"""

# セットへ要素を追加/削除
# セットへの要素の追加は、以下のように行うことができます。

# セットへ要素を追加
set_ = set()
set_.add("a")
print(set_) # {'a'}

# また、セットから要素を削除するには、以下の幾つかの方法があります。

set_ = set("abc")

# 指定した要素を削除する
set_.remove("b")
print(set_) # {'c', 'a'}

# しかし、removeを使うと、存在しない要素の場合にエラーになる
set_.remove("d")
# Traceback (most recent call last):
#   File "", line 1, in
# KeyError: 'd'

# 上記だとうざい場合は、代わりにdiscardを使うといいかも
set_.discard("a")
print(set_) # {'c'}
set_.discard("d") # エラーにならない
print(set_) # {'c'}

# 全部削除はこちら
# ただ、全部削除するなら、その変数を使わなければいいだけでもある
set_.clear()
print(set_) # set()

# と、このようにセットへの要素の追加/削除を行うことができます。

"""
set型の作り方

2つあります。
(1)要素をカンマで区切って”{　}”で囲う
"""

#｛｝で囲います
>>> s = {'one', 'two', 'three'}

#データ型を確認
>>> type(s)
# <class 'set'>

"""
(2)setコンストラクタを生成

class set([iterable])
class frozenset([iterable])

引数iterableから新しいset（またはfrozenset）オブジェクトを生成します。
iterableが空の場合は空の集合が返ります。
"""
#リストを例にします
>>> a = ['one', 'two', 'three']

#setオブジェクトの生成
>>> a_ = set(a)
>>> a_
{'one', 'two', 'three'}

#データ型を確認
>>> type(a_)
# <class 'set'>

#frozensetオブジェクトの生成
>>> f_ = frozenset(a)
>>> f_
frozenset({'one', 'two', 'three'})

#データ型を確認
>>> type(f_)
# <class 'frozenset'>

"""
set型の特徴

    順序がない
    可変（ミュータブル）
    重複がない
    イテラブルなコンテナオブジェクト
    集合演算が可能

以下、それぞれの特徴について詳細を示します。
"""

"""
(1)順序がない

setオブジェクトは、順序がありません。
よって、リストや文字列で使われるインデックス指定やスライス操作等のシーケンス的な操作はできません。
"""
#以下の集合a_を例にします
>>> a_
{'one', 'two', 'three'}

#インデックス指定はできません。
>>> a_[0]
Traceback (most recent call last):
File "", line 1, in
TypeError: 'set' object does not support indexing

"""
(2)可変(ミュータブル)

set型は（可変）ミュータブルなオブジェクトです。ミュータブルなため、

    ハッシュ値を持たず、辞書のキーや他の集合の要素として用いることができません。
    後からadd()やremove()メソッドで更新が可能です。

それぞれの例を以下に示します。
要素追加する：add(elem)

引数elemは追加したい要素を示します。
"""
>>> a_ = {'one', 'two', 'three'}

>>> a_.add('four')
>>> a_
{'one', 'two', 'four', 'three'}

"""
要素を削除する：remove(elem)

引数elemは削除したい要素を示します。
"""
>>> a_ = {'one', 'two', 'three'}
>>> a_.remove('one')
>>> a_
{'two', 'three'}

#elem が set に含まれていなければ KeyError を送出
>>> a_.remove('one')
Traceback (most recent call last):
File "", line 1, in
KeyError: 'one'

"""
要素を削除する：discard(elem)

removeメソッドとの違いは、elemがsetに含まれていない場合にNone返します。
"""
>>> a_ = {'one', 'two', 'three'}

>>> a_.discard('one')
>>> a_
{'two', 'three'}

#elem が set に含まれていなければNoneを返します
>>> a_.discard('one')
>>> print(a_.discard('one'))
# None

"""
任意の要素を取り除く：pop()

setから任意の要素を取り除き、それを返します。集合が空の場合、KeyError を送出します
"""
>>> a_ = {'one', 'two', 'three'}

>>> a_.pop()
'one'
>>> a_.pop()
'two'
>>> a_.pop()
'three'

#集合が空の場合エラーを送出
>>> a_.pop()
Traceback (most recent call last):
File "", line 1, in
KeyError: 'pop from an empty set'

#ちなみに引数は取りません
>>> a_
{'one', 'two', 'three'}
>>> a_.pop(1)
Traceback (most recent call last):
File "", line 1, in
TypeError: pop() takes no arguments (1 given)

"""
全ての要素を削除する：clear()
"""
>>> a_ = {'one', 'two', 'three'}
>>> a_.clear()
>>> a_
set()

"""
尚、同じ集合型でfrozenset型は不変でハッシュ可能(hashable)なので、
別の集合型の要素になったり、辞書のキーにすることができます。
frozensetオブジェクトは上記のaddやremoveなどで更新ができません。
"""
>>> f_
frozenset({'one', 'two', 'three'})

#frozensetオブジェクトはaddやremoveで更新ができません
>>> f_.add('four')
Traceback (most recent call last):
File "", line 1, in
AttributeError: 'frozenset' object has no attribute 'add'

>>> f_.remove('one')
Traceback (most recent call last):
File "", line 1, in
AttributeError: 'frozenset' object has no attribute 'remove'

"""
(3)重複がない

例えばリストから重複した要素を取り除くのに使えます。
"""
>>> l = ['one', 'two', 'three', 'one', 'two', 'three']
>>> set(l)
# {'one', 'two', 'three'}
"""
リストに変換すれば、重複を省いたリストが生成できます。

>>> list(set(l))
['one', 'two', 'three']
"""

"""
(4)イテラブルである

他のコンテナオブジェクト同様に、 x in set, len(set), for x in set が使えます。

    setオブジェクトの場合
"""

>>> a_ = {'one', 'two', 'three'}

>>> 'one' in a_
# True

>>> len(a_)
# 3

>>> for x in a_:
... print(x)
...
# one
# two
# three

# frozensetオブジェクトの場合
>>> f_
# frozenset({'one', 'two', 'three'})

>>> 'one' in f_
# True

>>> len(f_)
# 3

>>> for x in f_:
... print(x)
...
# one
# two
# three

"""
参考として、(3),(4)で挙げた性質を利用して、
リストの要素が全部同じかどうかを調べることができます。
つまり、重複を除いて出来た集合の長さが１の場合は、
要素が全て同じ、２以上なら異なる要素が含まれている。
"""
#リストの要素が異なる値の場合、長さが２以上
>>> a = [1, 1, 2, 1]
>>> len(set(a))
# 2

#リストの要素が全部同じ場合、長さが１
>>> b = [1, 1, 1, 1]
>>> len(set(b))
# 1


# 組み合わせと演算
# セットを使う理由の二つ目は、組み合わせ演算が非常に充実している点だと思います。
# 以下のように、和集合・差集合・積集合などを簡単に求めることができます。

# 積集合
# 2つのセットで共通した要素のみを抜き出すことができます。

# 積集合演算子

number1 = {1, 2, 3, 4, 5}
number2 = {3, 4, 5, 6, 7}

# 「&」演算子を使います
print(number1 & number2)
# {3, 4, 5}

# または「intersection」関数を使うこともできます
print(number1.intersection(number2))
# {3, 4, 5}

# 和集合
# 2つのセットを合算することができます。

# 和集合

number1 = {1, 2, 3, 4, 5}
number2 = {3, 4, 5, 6, 7}

# 「|」演算子を使います
print(number1 | number2)
# {1, 2, 3, 4, 5, 6, 7}

# または「union」関数を使います
print(number1.union(number2))
# {1, 2, 3, 4, 5, 6, 7}

# 差集合
# 引く対象のセットにしか存在しない値のみを抽出することができます。

# 差集合

number1 = {1, 2, 3, 4, 5}
number2 = {3, 4, 5, 6, 7}

# 「-」演算子を使います
print(number1 - number2)
# {1, 2}

# または「difference」関数を使います
print(number1.difference(number2))
# {1, 2}

# 排他的OR
# どちらか片方にしか含まれていない値を返します。

# 排他的OR（どちらか片方に含まれていて、両方には含まれない要素）

number1 = {1, 2, 3, 4, 5}
number2 = {3, 4, 5, 6, 7}

# 「^」演算子を使います
print(number1 ^ number2)
# {1, 2, 6, 7}

# または、「symmetric_difference」関数を使います
print(number1.symmetric_difference(number2))
# {1, 2, 6, 7}

# 部分集合のチェック
# 片方の集合が、もう片方の集合の部分集合であるかを検証することができます。

# 部分集合になっているかのチェック

number1 = {1, 2, 3, 4, 5}
number2 = {3, 4, 5, 6, 7}
number3 = {1, 2, 3}

# 「<=」演算子を使います
print(number3 <= number1)
# True
print(number1 <= number2)
# False

# 自分自身は部分集合なので、Trueを返します
print(number1 <= number1)
# True

# 新部分集合のチェック
# 片方の集合が、もう片方の集合の新部分集合であるかを検証することができます。

# 新部分集合のチェック

number1 = {1, 2, 3, 4, 5}
number2 = {3, 4, 5, 6, 7}
number3 = {1, 2, 3}

# 「<」を使います
print( number3 < number1)
# True

# 自分自身（=等価な物）は、「新」部分集合ではない
print(number1 < number1)
# False

# 上位集合のチェック
# 片方の集合が、もう片方の集合の上位集合であるかを検証することができます。

# 上位集合（部分集合の逆）

number1 = {1, 2, 3, 4, 5}
number2 = {3, 4, 5, 6, 7}
number3 = {1, 2, 3}

# 「>=」演算子を使います
print(number1 >= number3)
# True

# 自分自身は、上位集合である
print(number1 >= number1)
# True

# 新上位集合のチェック
# 片方の集合が、もう片方の集合の新上位集合であるかを検証することができます。

# 新上位集合

number1 = {1, 2, 3, 4, 5}
number2 = {3, 4, 5, 6, 7}
number3 = {1, 2, 3}

# 「>」演算子を使います
print(number1 > number1)
# True

# 自分自身（=等価な物）は、「新」上位集合ではない
print(number1 > number1)
# False

"""
まとめ

set型は集合を表すデータ型であり、以下の特徴を持っている。

    順序がない・・・リスト型とは異なりスライス操作が出来ないことに注意
    可変（ミュータブル）・・・add()やremove()でデータの更新が可能
    重複がない・・・データから重複を除くのに使える
    イテラブルなコンテナオブジェクト・・・forループで使える
    集合演算が可能・・・和集合、差集合等の数学的集合演算が可能
"""
