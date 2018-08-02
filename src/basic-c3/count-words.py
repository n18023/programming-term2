def display(moko , moko2) :
    print(moko , moko2)

# 単語の出現回数をカウント
text = """
Keep on asking, and it will be given you ;
Keep on seeking, and you will find ;
Keep on knocking, and it will be opened to you ;
for everyone asking receives , and everyone seeking finds ,
and to everyone knocking , it will be opened. """

# 単語を区切る
text = text.replace(';' , '') # ;を削除
text = text.replace(',' , '') # ,を削除
text = text.replace('.' , '') # .を削除
words = text.split() # 空白で区切ってリスト型を作成

# 単語を数える
counter = {} # counterと言う空の辞書型を作成
for _ in words :
    _s = _.lower() # 小文字に変換
    if _s in counter : # もし辞書型にすでにキーがあれば値を1つ追加
        counter[_s] += 1
    else :
        counter[_s] = 1 # もし辞書型にキーがなければ、値を1としてキーも登録

# 結果を表示
for k , v in sorted(counter.items()) : # counterのキーをアルファベット順として範囲に指定
    if v >= 3 :
        display(k , v)
