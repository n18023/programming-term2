def display(moko) :
    print(moko)
# 辞書型のデータ(果物名と値段)を変数に代入
fruits = {
    'バナナ':300 ,
    'オレンジ':240 ,
    'イチゴ':350 ,
    'マンゴー':400}

# 辞書型のデータ一覧を表示
for _ in fruits.keys() :
    # 値段を得る
    price = fruits[_]
    # 画面に出力
    s = "{0}は、{1}円です。".format(_ , price)
    display(s)
