import random
gamecontinue=True
while gamecontinue==True:
    print('数あてゲームスタート。3桁の数を当ててね')
    answer=[random.randint(0,9) for i in range(3)]
    prediction=[int(input(f'{i}桁目の予想>>')) for i in range(1,4)]
    hit=0
    boal=0
    print(f'正解は{answer}')
    print(f'予想は{prediction}')
    for i in range(3):
        if answer[i]==prediction[i]:
            hit+=1
        if answer[i] in prediction:
            boal+=1
    if hit==3:
        print('おみごと')
        gamecontinue=False
    else:
        print(f'結果は{hit}ヒット{boal}ボール')
        if int(input('続けますか？1:続ける2:終了>>'))==2:
            gamecontinue=False
