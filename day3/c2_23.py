scores={'network':60,'database':80,'security':60} #dictionary
members=['松田','浅木','工藤'] #list
print(tuple(members)) #リストmembersをタプルで作成
print(list(scores)) #scoresのキーをリストで作成
print(set(scores.values())) #scoresの値をセットで作成

#dictionaryの作成 dict(zip(,))
color_en=['red','green','blue']
color_ja=['赤','緑','青']
color=dict(zip(color_en,color_ja))
print(color)
