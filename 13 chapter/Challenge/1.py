"""
RectangleとSquareクラスを作る。両方のクラスに、その図形の外周の長さを
計算して返すcalculate_perimeterメゾットを定義する。
そして、RectangleとSquareオブジェクトを作って、
それぞれのcalculate_perimetterメゾットを呼ぶ。
calculate = 計算しなさい
perimetter = 周辺
Rectangle = 長方形
Square = 四角形
"""

class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return self.width * 2 + self.len * 2


class Rectangle(Shape):
    def area(self):
        return self.width * self.len

class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

a_rectangle = Rectangle(20, 10)
print(a_rectangle.calculate_perimeter())

a_square = Square(20)
print(a_square.calculate_perimeter())

"""
答え
class Rectangle():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2


class Square():
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

a_rectangle = Rectangle(25, 50)
a_square = Square(20)

print(a_rectangle.calculate_perimeter())
print(a_square.calculate_perimeter())
"""
