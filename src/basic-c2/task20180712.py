# 掛け算九九を表示するプログラム

str_line = 0
for x in range(1 , 10):
    for y in range(1 , 10):
        str_line = x * y
        str_line = str(str_line).rjust(3)
        print(str_line)
