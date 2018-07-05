# コンビニでの買い物

# 値段

beal_v = 200
otyumami_v = 100
yakitori_v = 100

# 個数

beal_c = 2
otyumami_c = 1
yakitori_c = 2

# 割引

yakitori_w = 1 - 0.2
point_kard = 150

# 計算

sum_v = ((beal_v * beal_c) + (otyumami_v * otyumami_c) + (yakitori_v * yakitori_c))
payment = (((beal_v * beal_c) + (otyumami_v * otyumami_c) + ((yakitori_v * yakitori_w) * yakitori_c)) - point_kard)

# 結果を表示

print('買い物の合計は' , sum_v , "円")
print('割引して貰うと' , payment , "円")
