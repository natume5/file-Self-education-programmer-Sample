# 関数内で変数を(print関数などで)使う場合問題なく動作する
def f():
    x = 1
    y = 2
    z = 3
    print(x)
    print(y)
    print(z)

f()
