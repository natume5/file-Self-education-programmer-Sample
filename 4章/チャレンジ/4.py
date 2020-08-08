"""
2つの関数からなるプログラムを書いてみる。
1つ目の関数は整数を引数として受け取り、
その整数を2で割って求められる整数を出力として返す。
2つ目の関数は整数を引数として受け取り、
4で掛けた整数を返す。
プログラム内で、1つ目の関数を呼び、戻り値を変数として保存し、
2つ目の関数の引数として渡す。
"""
def make_adder():
    print('加算関数を作成します')
    def add(x, y):
        z = x + y
        print('%d + %d = %d' % (x, y, z))
        return x + y
    return add

a = make_adder()
ans = a(1, 2)
print(ans)
"""
解説
1行目で外側の関数make_adderを宣言します。
3行目で内側の関数addを宣言します。
addは引数2つの和を返す関数です。
7行目がmake_adder関数の返り値で、add関数を関数オブジェクトとして返します。
9行目でmake_adder関数を呼び出し、戻り値を変数aに割り当てます。
10行目で変数a(関数オブジェクト)により、add関数を呼び出します。
"""
# 答え
def divide(x):
    return x / 2

def multiply(x):
    return x * 4

y = divide(4)
z = multiply(y)

print(z)
