class Rectangle:
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))

    def print_size(self):
        print("{}by{}".format(self.width, self.len))

r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs)

"""
このコードでは、クラスRectangleにクラスrecsを追加した。
クラス変数の定義は、__init__メゾットの外で行われる。
__init__が呼ばれるのは、クラスのインスタンスを作成した時だけです。
クラスオブジェクトを通してクラス変数にアクセスできるが、その時には、
__init__メゾットは呼ばれない。
　クラス定義の後に、Rectangleクラスのオブジェクト(=インスタンス)を
3つ作っている。それぞれのRectangleのインスタンスが作られるたびに
__init__メゾットが呼ばれ、幅と長さを含むタプルをrecsリストに追加している。
つまり、Rectangleのインスタンスが作られるたびにrecsリストに幅と長さのタプルが
追加される。
グローバル変数を使わずに、クラスのインスタンス間でデータを共有できる。
"""