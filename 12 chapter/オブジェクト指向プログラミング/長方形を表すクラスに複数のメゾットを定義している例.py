class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l

rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle.change_size(20, 40)
print(rectangle.area())

"""
この例では、Rectangleオブジェクトに2つのインスタンス変数lenとwidthがある。
areaメゾットは、2つのインスタンス変数を掛け算してRectangleオブジェクトの面積を返す。
change_sizeメゾットは、メゾットの引数に渡された値を
インスタンス変数lenとwidthに代入して変更する。
"""
