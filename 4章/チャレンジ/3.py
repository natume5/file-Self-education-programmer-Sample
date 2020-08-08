"""
3つの必須引数と2つのオプション引数がある関数を描いてみる。
"""
def f(x, y, z, a=10, b=20):
    return x + y + z + a + b

print(f(2, 3, 4))
print(f(5, 8, 10))

# 答え
def add_mult(a, b, c, x=100, z=1000):
    return a + b + c * x * z

result = add_mult(10, 15, 25)
print(result)
