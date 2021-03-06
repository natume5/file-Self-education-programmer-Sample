class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

lion = Lion("Dilbert")
print(lion)

"""
objectから継承した__repr__メゾットをオーバーライドすることで、
メゾットがLionオブジェクトの名前(=インスタンス変数name)を返すように変更した。
このため、Lionのオブジェクトを出力すると、<__main__.Lion object at 0x101178828>
のような文字列ではなく、名前(この例ではDilbert)が出力されるようになった。
演算子の対象となるオブジェクト(非演算子)は、演算子が式を評価するのに使用する
特殊メゾットを持つ必要がある。
例えば、2+2という式では、非演算子となるどちらの整数も特殊メゾット__add__を持っていて、
Pythonは足し算を評価するためにこのメゾットを呼ぶ。つまり、__add__メゾットをクラスに持たせれば、
そのオブジェクトを足し算の演算子で計算できるようになる。
"""