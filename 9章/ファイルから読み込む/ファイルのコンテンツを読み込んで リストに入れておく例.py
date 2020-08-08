my_list = []

with open("C:/Program Files/Sublime Text 3/"
          "Self-education programmer  Sample/9章/"
          "ファイルから読み込む/st.txt", "r", encoding="utf-8") as f:
    my_list.append(f.read())

print(my_list)
