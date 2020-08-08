"""
リストのリストに含まれている要素をcsvファイルに書き出そう。
データは次の通り
:[["Top Gun", "Risky Business", "Minority Reeport"],
["Titanic", "The Revenant", "Inception"],
["Training Day", "Man on Fire", "Flight"]]
データの各要素はcsvの一行となり、その一行に含まれる各要素がカンマで区切られるようにする。
"""
import csv


"""答え"""
movies = [["Top Gun", "Risky Business", "Minority Reeport"],
["Titanic", "The Revenant", "Inception"],
["Training Day", "Man on Fire", "Flight"]]
with open("movies.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    for movie_list in movies:
        spamwriter.writerow(movie_list)
