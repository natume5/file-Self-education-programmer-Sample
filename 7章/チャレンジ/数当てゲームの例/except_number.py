import random


random_num = random.randint(1, 5)
count = 0

while True:
    num = int(input("1から5までの数字を入力して下さい。"))

    if num == random_num:
        print("当たりです。")
        break
    else:
        print("はずれです。")
        print("もう一度入力して下さい。")
        count = count + 1

    if count == 5:
        print("ゲームオーバー")
        break
