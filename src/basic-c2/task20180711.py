# 入力値
hand = input('何を出しますか?1:グー、2:チョキ、3:パー')

# 関数
def moko():
    fmt = 'CPUが{cpu_hand}を出しました。貴方の負けです。'
    if hand == str(1):
        s = fmt.format(cpu_hand = 'パー')
        print(s)
    elif hand == str(2):
        s = fmt.format(cpu_hand = 'グー')
        print(s)
    elif hand == str(3):
        s = fmt.format(cpu_hand = 'チョキ')
        print(s)
    else:
        print('入力が不正です。終了します。')

# 出力結果
moko()
