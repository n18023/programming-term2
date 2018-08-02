def display(moko , moko2 , moko3) :
    print(moko , moko2 , moko3)
# あるクラスの国語テストの点数
points = [88 , 76 , 67 , 43 , 79 , 80 , 91]
sum_v = sum(points) # sum()関数で合計を求める
ave_v = sum_v / len(points)
display('合計点は' , sum_v , '点')
display('平均点は' , ave_v , "点")
