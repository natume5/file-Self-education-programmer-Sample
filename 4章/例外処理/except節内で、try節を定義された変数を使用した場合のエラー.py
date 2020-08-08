# except節内で、try節を定義された変数を使用した場合のエラー
try:
    10 / 0
    c = "I will never get defined."
except ZeroDivisionError:
    print(c)
