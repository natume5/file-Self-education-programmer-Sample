class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{}by{}".format(self.width, self.len))


class Square(Shape):
    def area(self):
        return self.width * self.len

    def print_size(self):
        print("I am {} by {}".format(self.width, self.len))

a_square = Square(20, 20)
a_square.print_size()

"""
この例では、親クラスにあるprint_sizeメゾットを同じ名前で子クラスに新しく定義して
メゾットオーバーライドした。
このため、このメゾットを呼ぶと新しいメッセージが出力されている。
"""