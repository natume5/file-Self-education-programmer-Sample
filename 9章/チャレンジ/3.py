"""
リストのリストに含まれている要素をcsvファイルに書き出そう。
データは次の通り
:[["Top Gun", "Risky Business", "Minority Reeport"],
["Titanic", "The Revenant", "Inception"],
["Training Day", "Man on Fire", "Flight"]]
データの各要素はcsvの一行となり、その一行に含まれる各要素がカンマで区切られるようにする。
"""
import csv


"""答え
movies = [["Top Gun", "Risky Business", "Minority Reeport"],
["Titanic", "The Revenant", "Inception"],
["Training Day", "Man on Fire", "Flight"]]
with open("mv.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    for movie_list in movies:
        spamwriter.writerow(movie_list)

"""
with open("mv.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=',')
    w.writerow(["Top Gun", "Risky Business", "Minority Reeport"])
    w.writerow(["Titanic", "The Revenant", "Inception"])
    w.writerow(["Training Day", "Man on Fire", "Flight"])
