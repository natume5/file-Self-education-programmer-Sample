class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)


x = AlwaysPositive(-20)
y = AlwaysPositive(10)


print(x + y)

"""
AlwaysPositiveのオブジェクトは__add__メゾットを持っているので、
足し算の演算子に対して被演算子として使える。
Pythonは足し算の式を評価するときに、演算子の左側のオブジェクトの__add__メゾットを呼び出す。
そして、演算子の右側のオブジェクトをそのメゾットに渡し、メゾットの戻り値を式の評価結果として使う。
　この例の__add__メゾットでは、2つの数値を足して、
その結果を組み込み関数absに渡して絶対値に変換している。
__add__メゾットを定義したことで、2つのAlwaysPositiveのオブジェクトを足し算演算子に渡すと、
計算結果は2つの数値の合計を絶対値にした値になる。
つまり、式の評価結果は必ず正の値になる。
"""