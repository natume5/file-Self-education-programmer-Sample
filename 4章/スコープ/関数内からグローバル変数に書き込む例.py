# 関数内からグローバル変数に書き込む例
x = 100

def f():
    global x
    x += 1
    print(x)

f()
