class Person:
    def __init__(self):
        self.name = 'Bob'

bob = Person()
same_bob = bob
print(bob is same_bob)


another_bob = Person()
print(bob is another_bob)

"""
式の中で、オブジェクトbobとsame_bobをisキーワードで比較すると、
2つの変数はPersonから作られた1つのオブジェクトを指しているので、
この式はTrueと評価される。
ここで、新しくもう一つのPersonのオブジェクトを作ってbobと比較してみる。
今度は、2つの変数が別のオブジェクトを指しているので、式にはFalseに評価される。
"""