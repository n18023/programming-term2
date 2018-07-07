# コンビニでの買い物

# 値段
beer_v = 200
otumami_v = 100
yakitori_v = 100

# 個数
beer_c = 2
otumami_c = 1
yakitori_c = 2

# 割引いた結果の率
yakitori_w = 1 - 0.2

# 計算
sum_v = ((beer_v * beer_c) + (otumami_v * otumami_c) + (yakitori_v * yakitori_c))
payment = (((beer_v * beer_c) + (otumami_v * otumami_c) + ((yakitori_v * yakitori_w) * yakitori_c)) - 150)

# 結果を表示
print('買い物の合計は' , int(sum_v) , "円")
print('割引して貰うと' , int(payment) , "円")
