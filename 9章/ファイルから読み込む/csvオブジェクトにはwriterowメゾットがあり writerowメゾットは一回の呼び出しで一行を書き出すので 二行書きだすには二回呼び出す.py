import csv


with open("C:/Program Files/Sublime Text 3/"
          "Self-education programmer  Sample/9章/"
          "ファイルから読み込む/st.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])

#  encoding="utf-8",
"""Pythonで開いたファイルのクローズを忘れやすい人のためのwith文の使い方
Pythonでwith文を使って安全にファイルを開いて閉じる方法

これまで本シリーズで紹介してきたテキストファイルの開き方と閉じ方は以下の通りでした。

f = open('area.txt')
# 処理
f.close()

open関数でファイルを開き、closeメソッドでファイルを閉じる。

ちゃんと書いたままにしておけばいいんですが、新しいスクリプトを書いてみたり、
あれこれしているうちに忘れてしまうんですよ、closeメソッド。

ファイルをクローズしないと

    システムのリソースを食ったまま
    他のプログラムがファイルにアクセスできなくなる
などのリスクがあります。

今回のようにローカルPCで、ファイル容量も少量で、
他のアプリケーションから使わないようなファイルであればさほど問題でもないのですが、
そうでもない場合にこの「忘れんぼ」がクセになっていると、よくないことが起きてしまいそうです。

ということで、転ばぬ先の杖。
ファイルを自動で閉じてくれるwith文の使い方をさっさとマスターしてしまいましょう。

with文を使ってファイルを開く方法

ファイルのオープンの場合を前提とすると以下のように記述します
with open(file, mode) as 変数:
　　# 処理

なんとこれだけで、以下と同様の処理になります。
変数 = open(file, mode)
# 処理
変数.close()

で、closeメソッドはどこ行っちゃったのだということなのですが、ご安心ください。
withブロックを抜けるときにcloseメソッドを勝手に呼び出して実行してくれるのです
しかも、with文にはもう一つ大きなメリットがあります。公式ドキュメントにはこうも書いてあります。

with を使うと、処理中に例外が発生しても必ず最後にファイルを閉じることができます。


with文でファイルを開く

ファイルオブジェクトが開いているかどうかは、closed属性を使って確認できます。
ファイルオブジェクト.closed

Trueなら閉じている、Falseなら閉じていない、つまり開いているとなります。
例えば、以下プログラムでいうと、一つ目のclosedはFalse、二つ目はTrueとなります。

f = open('area.txt') as f:
    print(f.closed)    # False
print(f.closed)    # True

では、with文を使ってファイルを開いた場合を見てみましょう

with open('area.txt') as f:
    print(f.closed)    # False
print(f.closed)    # True

withブロック内ではclosed属性はFalseとなっていますが、ブロックを抜けたらTrueですね。
ちゃんとクローズされているようです
"""
