for i in range(10):
    if i==7:
        break
    print(i)
else:
    print('終了')


import random
list=[]
for i in range(10):
    list.append(random.randint(0,9))
print(list)
if 7 in list:
    print('7ありました')
else:
    print('7ありませんでした')

#内包表記
list2=[random.randint(0,9) for i in range(10)]
print(list2)
