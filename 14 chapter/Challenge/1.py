"""
Squareクラスにsquare_listクラス変数を追加しよう。
そして、新しくSquareクラスのオブジェクトが作られるたびに、そのオブジェクトをこのリストに追加しよう。
"""
class Square:
    square_list = []

    def __init__(self, s):
        self.s = s
        self.square_list.append((self.s * 4))

    def print_size(self):
        print("{}by{}".format(self.s * 4))


s1 = Square(10)
s2 = Square(15)
s3 = Square(20)

print(Square.square_list)

"""
答え
class Shape():
    def what_am_i(self):
        print("I am a shape.")


class Square(Shape):
    square_list = []

    def __init__(self, s):
        self.s = s
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1 * 4

    def what_am_i(self):
        super().what_am_i()
        print("I am a Square.")


a_square = Square(29)
print(Square.square_list)
another_square = Square(93)
print(Square.square_list)
"""

"""
Squareクラスにsquare_listクラス変数を追加しよう。
そして、新しくSquareクラスのオブジェクトが作られるたびに、そのオブジェクトをこのリストに追加しよう。
"""

class Square:
    square_list = []

    def __init__(self, s):
        self.s = s
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s * 4

    def __repr__(self):
        return self.s


S2 = Square("12")
S3 = Square("20")
S4 = Square("30")

square_list = [S2, S3, S4]

for number in square_list:
    print(S2, S3, S4)

S5 = Square("14")
square_list.append(S5)

for number in square_list:
    print(S5)
