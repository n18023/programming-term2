# じゃんけんのプレイヤーの名前を第2引数で、nameという引数名で受け取れるように書き換えてください
def print_hand(hand , player_name):
    # 「(name)は(hand)を出しました」と出力されるように書き換えてください
    print(player_name + 'は' + hand + 'を出しました')

# 第2引数に文字列「ななしのたろう」を入れてprint_hand関数を呼び出すよう変更してください
print_hand('グー' , 'ななしのたろう')

# 第2引数に文字列「コンピューター」を入れてprint_hand関数を呼び出すよう変更してください
print_hand('パー' , 'コンピューター')
