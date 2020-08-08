class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{}by{}".format(self.wodth, self.len))

class  Square(Shape):
    def area(self):
        return self.width * self.len

a_square = Square(20, 20)
print(a_square.area())

"""
子クラスは親クラスのメゾットを継承しているが、このメゾット名と同じメゾットを
子クラスで定義することで上書きできる。
子クラスが親クラスのメゾットを別の実装で置き換えることをメゾットオーバーライド
と言います。
"""