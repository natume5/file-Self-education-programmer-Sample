import random
from time import sleep


OPENING_MESSAGE = """
-------------------------------
****数当てゲームへようこそ！*********
君は3桁の数字を当てることが出来るかな？

Hit = 桁と数字が当たっている
Blow = 数字が当たっている
数字 = 1~9が3桁　重複なし

-------------------------------
"""
# ゲームの中身
def game():
    # オープニング表示
    print(OPENING_MESSAGE)
    sleep(2)
    # 答えを作る処理
    kotae = []
    while len(kotae) != 3:
        x = random.randint(1, 9)
        if x not in kotae:
            kotae.append(x)

    # 回答回数カウント
    count = 5

    # ゲームの開始処理
    while True:
        # Hintの変数宣言と初期化
        H = 0
        B = 0

        # 入力処理
        kai = input("3桁の数字を入れてください。(残り' + str(count) + '回):")

        # 入力エラー処理
        # 数字以外
        if not kai.isdigit():
            print("数字以外は入力できません。")

        # 3桁以外の数字の場合
        elif len(kai) != 3:
            print("3桁の数字のみ入力して下さい。")

        # 入力値が正常の場合
        else:
            klist = list(map(int, kai))

            # 回答表示
            print(klist)

            # 答え合わせ
            for i, j in zip(klist, kotae):
                # ヒントの処理
                # Hit count
                if i == j:
                    H += 1

                # Blow count
                elif i in kotae:
                    B += 1

                else:
                    pass

            # ゲームクリアの処理
            if H == 3:
                print("おめでとうございます！")
                print("あなたは残り" + str(count) + "回でクリアしました！")
                break

            # ヒント出力
            print("Hit:" + str(H) + ' ' + "Blow:" + str(B))
            count -= 1

            # ゲームオーバーの処理
            if count == 0:
                print("残念！回答回数を超えました。")
                print("答え↓")
                print(kotae)
                break

    # ゲームの終了処理
    return print("ゲームを終了します。")

# ゲームの開始
def main():
    while True:
        # 初期処理
        x = input("プレイをしますか？　y/n:")

        # 例外処理
        if x != "y" and x != "n":
            print("yかnを入力して下さい。")

        # 終了処理
        elif x == "n":
            print("終了します。")
            break

        # 開始処理
        elif x == "y":
            print("起動します。")
            sleep(2)
            game()

        # 初期処理エラー
    else:
        print("不明なエラー")

if __name__ == "__main__":
    main()
