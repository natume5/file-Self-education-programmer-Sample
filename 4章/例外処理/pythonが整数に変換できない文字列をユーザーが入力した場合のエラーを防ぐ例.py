# pythonが整数に変換できない文字列をユーザーが入力した場合のエラーを防ぐ例
try:
    a = input("type a number:")
    b = input("type another:")
    a = int(a)
    b = int(b)
except(ZeroDivisionError, ValueError):
    print("Invalid input.")
