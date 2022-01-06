score=int(input('試験の点数>>'))
if score<0 or score>100:
    print('異常')
    print('入力し直し')
elif score>=60:
    print('合格')
    print('よく頑張りました')
else:
    print('不合格')
    print('追試です')
