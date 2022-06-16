#マイナンバー11桁を取得後、12桁目チェックデジットを求める計算
import sys

#文字の順番を逆にする
def nSwap(num):
    #tempNum
    tNum: str = str(11111111111)
    tmp_list= list(tNum)
    num_list = list(num)
    for i in range(11):
        tmp_list[i] = num_list[10-i]
    num = "".join(num_list)

    return tmp_list

#計算処理
#検査用数字 = 11−(∑n=1,11,Pn × Qnを11で除した余り)　ただし、計算結果が1以下の場合は0とする
#Pn = 個人番号を構成する検査用数字以外の11桁の番号の最下位の桁を1桁目としたときのn桁目の数字
#Qn = 1≦n≦6のときn+1、7≦n≦11のときn−5
def Calc(Pn):
    PnQn = 0
    for i in range(11):
        if i + 1 >= 1 and i + 1 <= 6:
            Pn[i] = int(Pn[i]) * (i + 2)
        elif i + 1 >= 7 and i + 1 <= 11:
            Pn[i] = int(Pn[i]) * (i - 4)
        
        PnQn += int(Pn[i])
        
    PnQn %= 11
    
    if PnQn <= 1:
        return 0
    else:
        return 11 - PnQn

#main
while True:
    try:
        #11桁を取得
        num: int = int(input('11桁の数字を入力してください>>>'))
        #stringnum
        sNum: str = str(num)
        if len(sNum) != 11:
            print('11桁の数字を入力してください')
            print('--------------------------------')
        elif len(sNum) == 11:
            break
     
    except ValueError:
        print('ValueError')
        sys.exit()

t_list = nSwap(sNum)
digit = Calc(t_list)

print("マイナンバー：" + sNum + str(digit))

