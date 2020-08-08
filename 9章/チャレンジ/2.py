"""
何か質問するプログラムを書こう。
入力された回答をファイルに書き出そう。
"""
answer = input("What is your favorite color?")
with open("C:/Program Files/Sublime Text 3/"
           "Self-education programmer  Sample/9章/st.txt", "w") as f:
    f.write(answer)

ans = input('今日の天気は？')
with open("C:/Program Files/Sublime Text 3/"
           "Self-education programmer  Sample/9章/st.txt", "w") as f:
    f.write(ans)
