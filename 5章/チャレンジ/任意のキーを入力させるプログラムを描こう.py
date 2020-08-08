"""
入力されたキーを使って、1つ前のチャレンジで用意した辞書から、
バリューを取得して表示する。
"""
me = {
    "1": ["height", "171cm"],
    "2": ["fav_color", "blue", "green"],
    "3": ["fav_musican", "Jonus blue", "Jax Joes", "Armin van Buuren", "kygo",
               "Alan Walker", "The Chainsmokers", "Mark Ronson",
               "Steve Aoki"]
}

my_list = [me]
my_list
my_tuple = (me,)
my_tuple

n = input("1~3の数字を入力してください。:")
if n in me:
    Feature = me[n]
    print(Feature)
else:
    print("見つかりませんでした。")
