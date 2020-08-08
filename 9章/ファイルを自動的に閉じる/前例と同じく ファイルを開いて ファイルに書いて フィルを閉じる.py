"""
ファイルをオーペンする時、ファイルの閉じ忘れを防止するもう一つの構文。
この構文では、ファイルオブジェクトを使う全てのコードをwith文の中に書く。
with文は複合文の一つで、処理がwithブロックを抜けたときに自動的に
指定した処理を実行する。
with文を使ってファイルを開く構文は
with open([ファイルパス], [モード]) as [変数名]:
    [コード]
"""

with open("C:/Program Files/Sublime Text 3/"
          "Self-education programmer  Sample/9章/"
          "ファイルを自動的に閉じる/st.txt", "w") as f:
    f.write("Hi from Python!")
