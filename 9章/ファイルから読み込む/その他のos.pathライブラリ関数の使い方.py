import os


path=os.path.join(os.path.abspath("."),"newfile.txt")

# ファイルサイズを取得
os.path.getsize(path)    # 15

# ファイル最終更新日時を取得する
time.ctime(os.path.getmtime(path))    # 'Sat Dec 15 16:58:21 2018'

# ファイル作成日時を取得する
time.ctime(os.path.getmtime(path))    # 'Sat Dec 15 16:47:01 2018'

# ファイルパスの分割
os.path.split(path)    # ('/home/myUserID/', 'newfile.txt')
