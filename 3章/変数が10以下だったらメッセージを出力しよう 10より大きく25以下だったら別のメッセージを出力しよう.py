"""
変数が10以下だったらメッセージを出力しよう。
10より大きく25以下だったら、別のメッセージを出力しよう。
25より大きかったらさらに別のメッセージを出力しよう。
"""

x = 8
if x <= 10:
    print("xは10以下です。")
elif x <= 25:
    print("xは10より大きいです。しかし、25より小さいです。")
else:
    print("xは25より大きいです。")
