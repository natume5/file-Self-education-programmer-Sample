"""
六角形を表すHexagonクラスを定義しよう。
そのクラスには、外周の長さを計算して返すメゾットcalculate_perimeterを定義する。
そして、Hexagonオブジェクトを作って、calculate_perimeterメゾットを呼び出し、
結果を出力する。
"""

import math


class Hexagon:
    def __init__(self, )

"""答え
class Hexagon():
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6

a_hexagon = Hexagon(1, 2, 3, 4, 5, 6)
print(a_hexagon.calculate_perimeter())
"""