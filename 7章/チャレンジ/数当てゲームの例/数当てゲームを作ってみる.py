from random import randint


# オープニングメッセージの処理
openingmessage="""数当てゲームの世界へようこそ！
このゲームでは、コンピュータが１〜９９までの数字のうち一つを指定します。
解答欄に自分が正解だと予想する数字を入力してください。
あなたが選んだ数字がコンピュータが選んだ数字と一致していれば「正解！！」
あなたの数字の方がコンピュータが選んだ数字より大きければ「もっと下！！」
あなたの数字の方がコンピュータが選んだ数字より小さければ「もっと上！！」と出てきます。"""

# オープニングメッセージの表示
print(openingmessage)

# 答えの作成
answer = randint(1,99)

# カウント回数の作成
count = 1

while True:
    kai= input('予想した数字を入力してください！（' + str(count) +'回目):')
    print(kai)# 解答の入力欄の表示

    if not kai.isdigit():
        print('１〜９９の数字のみ入力可能です')
    elif len(kai)>2:
        print('１〜９９の数字のみ入力可能です')
       # 例外処理（上は解が数字出ないパターン、下は解が３桁以上だったパターン）

    else:
        n = int(kai)
      # kotaekist = list(map(int,kai))

        count += 1    # ターンをプラスする

        if n > answer:
            print('もっと下！！')

        elif n < answer:
            print('もっと上！！')

        else:
            n = answer
            print('正解！！')
            break


print('答えは{}、かかったターンは{}ターンでした！'.format(answer,count-1))
