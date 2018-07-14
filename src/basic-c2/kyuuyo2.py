# 時給計算プログラム

# 時給の入力
user = input('時給はいくらですか?')
jikyuu = float(user)

# 時間の入力
user = input('何時間働きましたか?')
jikann = float(user)

# 計算
kyuuryou = jikyuu * jikann

# 結果を表示
fmt = """
時給{0}円で、{1}時間働いたので...
給料は、{2}円です。
"""
desc = fmt.format(jikyuu , jikann , kyuuryou)
print(desc)
