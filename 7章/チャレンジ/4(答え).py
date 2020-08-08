"""
無限ループする数字当てプログラムを書こう。
ユーザーに文字を入力してもらい、qが入力されたら終了、数字が入力されたら正解かどうか判定する。
正解の数値はプログラム内に幾つかリストを持たせておいて、ユーザーが入力した数字とどれかが一致したら
正解、一致しなかったら不正解と表示する。
もしq以外の文字が入力されたら、「数字を入力するか、qで終了します。」
と表示しよう。
"""
numbers = [11, 32, 33, 15, 1]

while True:
    answer = input("Guess a number or type q to quit.")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("please type a number or 'q' to quit.")
    if answer in numbers:
        print("You gussed correctly!")
    else:
        print("You gessed incorrectoly!")
