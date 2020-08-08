class Lion:
    def __init__(self, name):
        self.name = name


lion = Lion("Dilbert")
print(lion)

"""
Lionのオブジェクト(=インスタンス)をprint関数に渡すと、Pythonはobjectクラスから継承した
__reper__という特殊メゾットを呼び出します。それから__reper__が返してきた値を出力する。
この__reper__メゾットをオーバーライドして出力したい内容を変更で出来る。
"""
