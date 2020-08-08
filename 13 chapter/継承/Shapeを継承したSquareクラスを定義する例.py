class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{}by{}".format(self.width, self.len))


class Square(Shape):
    pass

a_square = Square(20, 20)
a_square.print_size()

"""
Squareクラスの定義でパラメータにShapeクラスを指定したので、
SquareクラスはShapeクラスの変数とメゾットを継承しました。
クラスを定義するときにpassというキーワードを使っているが、
これによりPythonに何もしなくていいことを伝ええています。
継承した結果、幅と長さを渡してSquareオブジェクトを作成できるようになりました。
また、Squareクラスに実装していないprint_sizeメゾットも使える。
このようなコードの削減によって、同じコードを何度も書かなくてよくなり、
コード全体が小さくなればより扱いやすくなる。
　子クラスには、他のクラス定義のようにメゾットや変数を定義できる。
これらは親クラスには影響しない。
"""