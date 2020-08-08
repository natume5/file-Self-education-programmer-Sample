"""
Squareクラスにchange_sizeメゾットを定義して、そこに渡した数値の分だけ
Squareオブジェクトのオブジェクトの横幅を増やしたり、減らしたり(マイナス値の場合)して
みよう。
Square = 四角形
"""

class Square():
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, new_size):
        self.s1 += new_size


a_square = Square(100)
print(a_square.s1)

a_square.change_size(200)
print(a_square.s1)

"""
答え
class Square():
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, new_size):
        self.s1 += new_size

a_square = Square(100)
print(a_square.s1)

a_square.change_size(200)
print(a_square.s1)
"""