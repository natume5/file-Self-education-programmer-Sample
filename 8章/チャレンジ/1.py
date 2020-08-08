"""
statisticsモジュールの別の関数を呼んでみる。

平均及び中心位置の測度
これらの関数は母集団または標本の平均値や標準値を計算します。

mean()        データの算術平均。算術平均はデータの総和をデータ数で除したものです。
　　　　　　　　単に「平均」と呼ばれることも多いですが、数学における平均の一種に過ぎません。
　　　　　　　　データの中心位置の測度の一つです。


fmean()       Fast, floating point arithmetic mean.

geometric_mean()       Geometric mean of data.

harmonic_mean()      データの調和平均。

median()       データの中央値。

median_low()     median_lowはデータ数が奇数の場合は中央の値を返し、
　　　　　　　　　偶数の場合は中央の2値の小さい方を返します。
　　　　　　　　　データが離散的で、中央値が補間値よりもデータ点にある値の方が
　　　　　　　　　良い場合に用いてください。

median_high()     median_highはデータ数が奇数の場合は中央の値を返し、
　　　　　　　　　　偶数の場合は中央の2値の大きい方を返します。

median_grouped()   grouped data の中央値、すなわち50パーセンタイル。

mode()    Single mode (most common value) of discrete or nominal data.

multimode()    List of modes (most common values) of discrete or nomimal data.

quantiles()    Divide data into intervals with equal probability.
"""
import statistics


data = [14, 3, 11, 133, 4]

result = statistics.median_low(data)

print(result)


mean([1, 2, 3, 4])
print(mean)    # 2.8

mean([-1.0, 2.5, 3.25, 5.75])
print(mean)    # 2.625

from fractions import Fraction as F
fc = mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)])
print(fc)    # Fraction(13, 21)

from decimal import Decimal as D
dm = mean([D("0.5"), D("0.75"), D("0.625"), D("0.375")])
print(dm)    # Deccimal(0.5625)

hm = harmonic_mean([40, 60])
print(hm)

md = median([1, 3, 5])
print(md)    # 3

# データ数が偶数の場合は、中央値は中央に最も近い2値の算術平均で補間されます
md = ([1, 3, 5, 7])
print(md)    # 4.0
# データが離散的で、中央値がデータ点にない値でも構わない場合に適しています。

mg = median_groupe([1, 2, 2, 3, 4, 4, 4, 4, 5])
print(mg)    # 3.7

mg = median_grouped([1, 3, 3, 5, 7], interval=1)
print(mg)    # 3.25

mg = median_grouped([1, 3, 3, 5, 7], interval=2)
print(mg)    # 3.5
