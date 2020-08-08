class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n

# インスタンス変数numsを直接変更する方法
# numsをリストからタプルに変更しようとした場合こちらは正しく動作しなくなる
data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)

# change_dataメゾットを使う方法
# プライベートであればオブジェクトの外から利用されることはないので
# clientのコードを壊すような心配はない
# client=クラスの外からオブジェクトを利用するコード
data_two = Data()
data_two.change_data(0, 100)
print(data_two.nums)
