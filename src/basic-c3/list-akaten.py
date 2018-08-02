def display(moko) :
    print(moko)

# 国語の点数の一覧
points = [80 , 40 , 23 , 14 , 29 , 58]

# 30点未満のデータだけ選んで赤点リストに追加
akaten = []
for _ in points :
    if _ < 30 :
        akaten.append(_)

# 選んだデータを表示
display(akaten)
