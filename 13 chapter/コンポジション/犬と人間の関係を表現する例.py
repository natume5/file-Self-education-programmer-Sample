class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self, name):
        self.name = name

mick = Person("Mick Jagger")
stan = Dog("Stanley", "Bulldog", mick)
print(stan.owner.name)

"""
コンポジションは「has-a関係」を表し、別クラスのオブジェクトを変数として持たせる。
例えば、犬とその飼い主という関係を表すのにコンポジションを使い、
犬は1人の飼い主を持つ、と表現する。
そして、Dogオブジェクトの作成時にその犬の飼い主としてPersonオブジェクトを
渡す。
"Stanley"という名前のstanオブジェクトは、"Mick Jagger"という名前のPersonオブジェクトを
インスタンス変数ownerに持つ。
"""