def display(moko , moko2 , moko3) :
    print(moko , moko2 , moko3)
# あるクラスの国語テストの点数をリストに代入
points = [88 , 76 , 67 , 43 , 79 , 80 , 91]
# テストの合計を求める
sum_v = 0
for _ in points :
    sum_v += _
    display(_ , '点を足して合計は' , sum_v)

# 平均を求める
ave_v = sum_v / len(points) # 平均 = 合計 / 点数の数
display('平均点は' , ave_v , "点")
