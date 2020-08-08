import os


with open("area.txt") as f:
    areas = f.readlines()
for area in areas:
    area = area.rstrip()
    if os.path.exists(area):
        print('フォルダ' + area + 'は既に存在しています')
    else:
        os.mkdir(area)
