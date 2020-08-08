pop = []     # 洋楽ポップソングを保存するリスト
jpop = []    # Jpopソングを保存するリスト

def collect_songs():
    song = "曲名を入力して下さい:　"
    ask = "pかqのどちらかを入力して下さい。qで終わります。:　"

    while True:
        genre = input(ask)
        if genre == "q":
            break

        if genre == "p":
            p = input(song)
            pop.append(p)

        elif genre == "j":
            j = input(song)
            jpop.append(j)

        else:
            print("不正な値です。")
    print("pop songs:", pop)
    print("jpopsongs:", jpop)

collect_songs()
