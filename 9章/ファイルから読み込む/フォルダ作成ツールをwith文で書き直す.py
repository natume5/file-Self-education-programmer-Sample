"""
ということで、今までのフォルダ作成ツールのテキストファイルを開く処理について、with文で書き直してみます。

テキストファイルからreadメソッドを使って、テキストファイルをまとめて文字列として
読み込むパターンはこうなりますね。

"""
import os


with open("area.txt") as f:
    areas = f.read().split()
for area in areas:
    if os.path.exists(area):
        print('フォルダ' + area + 'は既に存在しています')
    else:
        os.mkdir(area)
