"""
リスト["The", "fox", "jumpped", "over", "the", "fence", "."]
の文字列を正しい英文になるようにしよう。
単語と単語の間は空白が必要ですが、最後のピリオドの前には空白は不要です。
文字列を要素に持つリストを1つに連結するメゾットがあることを忘れずに！
"""
list = ["The", "fox", "jumped", "over", "the", "fence", "."]
a = " ".join(list)
a = a[0:-2] + "."
print(a)

# 答え
fox = ["The", "fox", "jumped", "over", "the", "fence", "."]
fox = " ".join(fox)
fox = fox[0:-2] + "."
print(fox)
