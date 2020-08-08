"""
2つの文字列を出力させるプログラムを書こう。
その文字列をそれぞれ、別の文字列の2つの個所に穴埋めした新しい文字列を作ろう。
"私は昨日[入力1]を書いて、[入力2]に送った！"
そして、それを出力しよう。
"""
what = input("何を:")
who = input("誰に:")

r = "私は昨日{}を書いて、{}に送った！".format(what, who)
print(r)

# 答え
answer1 = input("what did you write yesterday?")
answer2 = input("what did you go yesterday?")

new_string = "Yesterday I wrote a {}.I sent it to {}".format(answer1, answer2)
print(new_string)
