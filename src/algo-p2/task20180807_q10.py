# 文字列のキーと数値の値を持つ辞書を作って、変数itemsに代入してください
# appleは100円、bananaは200円、orangeは400円です。
items = {'apple':100 , 'banana':200 , 'orange':400}

# for文を用いて、辞書itemsのキーを1つずつ取り出していく繰り返し処理を作成してください
for fruits_key in items.keys() :
    # 「---------------------------------------------」を出力してください
    print('---------------------------------------------')
    # 「◯ ◯ は1個△ △ 円です」となるように出力してください
    print(fruits_key + 'は1個' + str(items[fruits_key]) + "円です")
