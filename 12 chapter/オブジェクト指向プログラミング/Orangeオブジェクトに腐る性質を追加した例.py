class Orange:
    def __init__(self, w, c):
        """weight(重さ)はグラム"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        """temp(湿度)は摂氏"""
        self.mold= days * temp

orange = Orange(200, "orange")
print(orange.mold)
orange.rot(10, 37)
print(orange.mold)

"""
メゾットrotは、オレンジを買ってからの日数と、その期間の平均温度の2つの引数を受け取る。
このメゾットは、2つの引数からインスタンス変数modを計算して代入する。
このように、メゾット内ではインスタンス変数を変更できる。
これで、オレンジに腐る性質を追加することが出来ました。
"""