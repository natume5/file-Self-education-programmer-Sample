# 関数なしで記述されたプログラムの例の機能を関数にまとめた例
def even_odd():
    n = input("type a number:")
    n = int(n)
    if n % 2 == 0:
        print("n is even.")
    else:
        print("n is odd.")

even_odd()
even_odd()
even_odd()
