# クラス内部のデータをclientから直接操作できるようにしたい時はパブリック変数を使う
class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"    # (オブジェクトの)外から使っても(アクセス)いい
        self._unsafe = "unsafe"    # 安全じゃない、外から使われることを想定していない
        # Pythonのプログラマーは変数やメゾットがアンダースコアで始まっていたら
        # 触ってはいけない(オブジェクトの外からアクセスしてはいけない)と知っている

    def public_method(self):
        # clientが使ってもよい
        pass    # pass文は、文が必須な構文でも何もしない場合に使う

    def _unsafe_method(self):
        # clientは使うべきじゃない
        pass    # pass文は、文が必須な構文で何もしない場合に使う
