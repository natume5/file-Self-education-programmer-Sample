# Python のリストにクラスのオブジェクトを入れる
# 新しいメンバーがやってきてもappend()を使えば対処できます．

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email


Taro = Person("Taro", "Taro@python.com")
Jiro = Person("Jiro", "Jiro@python.com")

Person_info = [Taro, Jiro]

#Add from here

Saburo = Person("Saburo", "Saburo@python.com")
Person_info.append(Saburo)

#Add until here

for member in Person_info:
    print("Name:", member.name, " Email:", member.email)
