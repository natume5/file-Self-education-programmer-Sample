# ここで開くファイルは、
# 前のコード例を実行して
# 作られる。

import csv


with open("C:/Program Files/Sublime Text 3/"
          "Self-education programmer  Sample/9章/"
          "ファイルから読み込む/st.csv", "r") as f:
    r = csv.reader(f, delimiter=',')
    for row in r:
        print(",".join(row))

"""
この例では、csvファイルを開いて、csv.readerメゾットでcsvオブジェクトに
変換して読み込んでいる。csvオブジェクトをforループで繰り返す。
ループごとに、取り出されたrowの要素をカンマで結合して、出力している。
これで、ファイルに書かれているコンテンツと同じように、カンマで区切られた文字列を
再現できる。
"""
