# coding: UTF-8
# 掛け算九九

str_line = ''
for x in range(1 , 10):
    str_line = ''
    for y in range(1 , 10):
        crossed = x * y
        str_line = str_line + str(crossed).rjust(3)
    print(str_line) # ここまで出来ました
