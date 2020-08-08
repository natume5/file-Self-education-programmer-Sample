from random import randint


qa = randint(1, 30)
count = 3
n = 0
while True:    # 無限ループ
    ans = input("30までの数値を入力してください。qで終了します。解答:")
    if ans == "q":
        break
    if ans in ["qa"]:
        print("正解！")
        break
    else:
        print("ハズレ。")
        count -= 1
        n = n + 1
    if ans > "qa":
        print("もっと下!")
    elif ans < "qa":
        print("もっと上!")
    if count == 0:
        print("ゲームオーバー")
        break

print('答えは{}'.format(qa))