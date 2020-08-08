"""
三角形を表すTriangleクラスを定義して、面積を返すareaメゾットを持たせよう。
そして、Triangleオブジェクトを作って、areaメゾットを呼び出して、結果を出力しよう。
"""
import math


class Triangle:
    def __init__(self, b, h):
        self.bottom = b
        self.hight = h

    def area(self):
        return self.bottom * self.hight / 2

    def change_size(self, b, h):
        self.bottom = b
        self.hight = h

triangle = Triangle(10, 5)
print(triangle.area())

"""答え
class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.height * self.base / 2

a_triangle = Triangle(20, 30)
print(a_triangle.calculate_area())
"""