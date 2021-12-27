language=int(input('国語>'))
mathematic=int(input('算数>'))
science=int(input('理科>'))
society=int(input('社会>'))
english=int(input('英語>'))
scores=[language,mathematic,science,society,english]
total=sum(scores)
average=total/len(scores)
print(f'合計は{total}点、平均は{average}')

