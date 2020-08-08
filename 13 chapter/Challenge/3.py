"""
Shapeクラスを定義しよう。呼ばれたら"I am shape"を返すメゾットwhat_am_iを定義しよう。
前のチャレンジで定義したRectangleとSquareクラスを変更して、このShapeクラスを継承させよう。
そして、RectangleとSquareのオブジェクトを生成して、このチャレンジで追加したメゾットwhat_am_iを
呼んでみる。
"""
class Shape():
    def what_am_i(self):
        print("I am a shape.")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2


class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

a_rectangle = Rectangle(10, 10)
print(a_rectangle.what_am_i())

a_square = Square(20)
print(a_square.what_am_i())

"""
答え
class Shape():
    def what_am_i(self):
        print("I am a shape.")


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2


class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

a_rectangle = Rectangle(20, 50)
a_square = Square(29)

a_rectangle.what_am_i()
a_square.what_am_i()
"""
