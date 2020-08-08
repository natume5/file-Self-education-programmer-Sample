with open("C:/Program Files/Sublime Text 3/"
          "Self-education programmer  Sample/9章/"
          "ファイルから読み込む/st.txt", "r", encoding="utf-8") as f:
    print(f.read())

"""
ファイルがアスキー文字のみで書かれている場合でも、この開き方で問題ありません。
もし、Windowsでよく使われているシフトJISでファイルが書かれている場合、
encodingに"cp932"を指定する。

readメゾットは、ファイルを開いた後一回だけ使える。
もう一度コンテンツ(内容)を読み込みたい場合は、
ファイルをいったん閉じてから、もう一度開いてください。

readメゾットで読み込んだファイルのコンテンツは、
後で使いやすいように変数やコンテナに入れておくといい。
"""
