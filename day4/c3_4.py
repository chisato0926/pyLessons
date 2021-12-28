name=input('名前＞')
print(f'{name}さんこんにちは')
food=input(f'{name}さんの好きな食べ物＞')
if 'カレー' in food:
    print('素敵です！')
else:
    print(f'私も{food}が好きですよ！')

n=10
if n in [5,10,15]:
    print('ok')
else:
    print('no')

key='red'
if key in {'red':'赤','blue':'青'}:
    print('ok')
else:
    print('no')
