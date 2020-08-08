"""
Squareクラスのオブジェクトをprint関数に渡したら、4辺それぞれの長さを出力しよう。
例えば、Square(29)のようにオブジェクトを作ったら、print関数では29by29by29by29と出力しよう。
Square(四角形)
"""

class Square:
    recs = []

    def __init__(self, s1):
        self.s1 = s1
        self.recs.append((self.s1 * 4))

    def print_size(self):
        return"{}by{}by{}by{}".format(self.s1, self.s1, self.s1, self.s1)

all_square = Square(29)
print(all_square.print_size())

"""
答え
class Shape():
    def what_am_i(self):
        print("I am a shape.")


class Square(Shape):
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1 * 4

    def what_am_i(self):
        super().what_am_i()
        print("I am a Square.")

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)

a_square = Square(29)
print(a_square)
"""
