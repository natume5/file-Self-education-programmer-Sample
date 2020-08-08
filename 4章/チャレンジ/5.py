"""
文字列をfloat型に変換して戻り値とする関数を書いてみる。
起こりうる例外をキャッチする例が処理を描く。
"""
# python3 文字列をfloat型に変換して関数を書いてみる
num = float("3.6")
ans = num + 5.1
print(ans)

# 答え
def convert(string):
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string to a float.")

c = convert("55.0")
print(c)
