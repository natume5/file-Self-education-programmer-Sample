"""
リンゴと言われて思い浮かぶ、4つの属性を考える。
その4つの属性をインスタンス変数に持つAppleクラスを定義する。
"""

class Apple:
    def __init__(self, w, c, p, d):
        """weight(重さ)はグラム"""
        self.weight = w
        self.color = c
        self.producing = p
        self.date = d
        print("Created!")

ap1 = Apple(400, "red", "青森", "11月10日")
ap2 = Apple(380, "red", "長野", "10月30日")
ap3 = Apple(410, "green", "岩手", "10月29日")
ap4 = Apple(390 , "red&green", "山形", "11月3日")

"""答え
class Apple():
    def __init__(self, color, weight, stem_length, circumference):
        self.color = color
        self.weight = weight
        self.stem_length = stem_length
        self.circumference = circumference
"""
