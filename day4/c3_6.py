scores={'network':60,'database':80,'security':50,'python':80}
key=input('追加する科目名＞＞')
if key in scores:
    print('すでに登録済み')
else:
    data=int(input('得点＞＞'))
    scores[key]=data
print(scores)
