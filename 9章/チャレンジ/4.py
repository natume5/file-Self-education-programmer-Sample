"""
チャレンジ3を日本語で同じようにやってみよう。
例えば、"Top Gun"を"トップガン"のように日本語に置き換えて、
csvファイルに書き出そう。
"""
import csv


movies = [["トップガン", "卒業白書", "マイノリティリポート"],
          ["タイタニック", "レヴェナント", "インセプション"],
          ["トレーニングデイ", "マイ・ボディガード", "フライト"]]
with open("映画.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    for movie_list in movies:
        spamwriter.writerow(movie_list)
