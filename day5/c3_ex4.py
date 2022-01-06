month=int(input('今は何月ですか？＞＞'))
if month in[1,3,5,7,8,10,12]:
    print('31日までありますね')
else:
    if month!=2:
        print('30日までですね')
    else:
        print('1年で一番寒い時期ですね')
    print('年が明けてから')
print(f'{month}カ月が過ぎました')
