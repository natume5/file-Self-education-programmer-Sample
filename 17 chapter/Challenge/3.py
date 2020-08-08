"""
Pythonのreモジュールを使って、何かの文字の後にoが2回登場する単語に一致する
正規表現を書こう。
そして、"The ghhost that says boo haunts the loo"の文中に
あるbooやlooに一致するか試そう。
"""
import re


string = "The ghhost that says boo haunts the loo"
m = re.findall("[bl]oo", string, re.IGNORECASE)
print(m)
