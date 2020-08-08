"""
HorseクラスとRiderクラスを定義する。
コンポジションを使って、馬(Horse)に騎手(Rider)を持たせよう。
"""

class Horse:
    def __init__(self, name, color, owner):
        self.name = name
        self.color = color
        self.owner = owner

class Rider:
    def __init__(self, name):
        self.name = name

Michael = Rider("Michael Stoute")
OperaHouse = Horse("Opera House", "Bay", Michael)
print(OperaHouse.owner.name)

"""
答え
class Horse():
    def __init__(self, name):
        self.name = name


class Rider():
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse

harry_the_horse = Horse("Harry")
the_rider = Rider("Sally", harry_the_horse)

print(the_rider.horse.name)
"""