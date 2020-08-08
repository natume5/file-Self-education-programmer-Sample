"""
円を表すCircleクラスを定義しよう。そのクラスに、面積を計算して返すメゾットareaを持たせよう。
面積の計算には、Pythonの組み込みモジュールmathのpi定数が使える。
次に、Circleオブジェクトを作って、areaメゾットを呼び出し、
結果を出力する。
"""

import math


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * math.pi

    def change_size(self, r):
        self.radius = r

circle = Circle(10)
print(circle.area())
circle.change_size(4)
print(circle.area())

"""答え
import math


class Circle():
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.radius ** 2 * math.pi

a_circle = Circle(4)
print(a_circle.calculate_area())
"""