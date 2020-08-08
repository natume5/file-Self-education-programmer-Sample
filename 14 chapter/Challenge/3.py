"""
2つのパラメーターを受け取る関数を書こう。この関数は同じオブジェクトを渡されたら
Trueで返し、そうじゃなかったらFalseで返そう。
"""
class Person:
    def __init__(self):
        self.name = 'Bob'

bob = Person()
same_bob = bob
print(bob is same_bob)


another_bob = Person()
print(bob is another_bob)

"""
答え
def compare(obj1, obj2):
    return obj1 is obj2

print(compare("a", "b"))
"""