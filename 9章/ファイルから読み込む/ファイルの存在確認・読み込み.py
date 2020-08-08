"""
ファイルパスを生成し、該当のパスにファイルが存在すれば読み込みを行うプログラムをコーディングします。
"""

#ファイルパスの取得(先ほどの例と同じ処理)
path = os.path.join(os.path.abspath("."),"newfile.txt")
print(path)    # '/home/myUserID/newfile.txt'

# ファイルの存在確認
os.path.isfile(path)    # True

#ファイルが存在するかチェックし、存在すれば読み込みを行う
if os.path.isfile(path):
    f = open(path,'r')
    f.read()
    f.close()    # 'new test file.\n'
