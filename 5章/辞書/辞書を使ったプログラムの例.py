songs = {"1": "fun",
         "2": "blue",
         "3": "me",
         "4": "floor",
         "5": "live",
         }

n = input("数字を入力して下さい:")
if n in songs:
    songs = songs[n]
    print(songs)
else:
    print("見つかりません。")

