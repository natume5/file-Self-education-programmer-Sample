# grepを使って、文字列"Arizona 479,501,870.California 209,213,650."にある、
# 数字の部分全てに一致する正規表現を書こう。
import re


line = "Arizona 479,501,870.California 209,213,650."
m = re.findall("\d", line, re.IGNORECASE)
print(m)

# ['4', '7', '9', '5', '0', '1', '8', '7', '0', '2', '0', '9', '2', '1', '3', '6', '5', '0']
