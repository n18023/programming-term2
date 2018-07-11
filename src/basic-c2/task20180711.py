# 入力値
hand = input('何を出しますか?1:グー、2:チョキ、3:パー')

# 結果のメッセージ
def display(moko2):
    print(moko2)

# 関数
def moko():
    hand
    if hand == str(1):
        display('CPUがパーを出しました。貴方の負けです。')
    elif hand == str(2):
            display('CPUがグーを出しました。貴方の負けです。')
    elif hand == str(3):
                display('CPUがチョキを出しました。貴方の負けです。')
    else:
        display("入力が不正です。終了します。")

moko()
