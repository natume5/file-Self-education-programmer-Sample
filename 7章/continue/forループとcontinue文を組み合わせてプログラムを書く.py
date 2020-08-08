"""
1から5までの数字を出力したいが3はのぞきたい。
"""
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
