"""
1から5までの数字を出力したいが3はのぞきたい。
forループとcontinue文を組み合わせたプログラム
"""
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
