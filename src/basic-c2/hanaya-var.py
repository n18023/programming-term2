#print(((500 *18) +(400 *(8 -2) +(700 *(21 -5)) *(1 -0.1))

# 花屋の支払金額を求める


# 値段

rose_v =500
sun_v =400
turip_v =700

# 個数

rose_c =18
sun_c =8 -2
tulip_c =21 -5

# 割引率

rate =1 -0.1

# 計算

sum_v =(rose_v *rose_c) +(sun_v *sun_c) +(tulip_v *tulip_c)
payment =sum_v *rate

# 結果を表示

print('買い物の合計は' ,sum_v ,"円")
print('割引して貰うと' ,payment ,"円")
