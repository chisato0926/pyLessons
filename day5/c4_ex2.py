count=0
print('カレーを召し上がれ')
while True:
    print(f'{count}皿のカレーを食べました')
    ans=input('おかわりはいかがですか？(y or n)＞＞')
    if ans=='y':
        count+=1
    else:
        break
print('ごちそうさまでした')
