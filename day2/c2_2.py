members=['工藤','松田','浅木'] #リスト作成
print(members) #リスト参照
print(members[0]) #リストの要素参照
print(len(members)) #要素数
members.append('山田') #要素の追加
print(members)
members[3]='山崎' #要素の書き換え
print(members)
members.remove('山崎') #要素の削除
print(members)
del members[0] #index指定での削除
print(members)

nums=[10,20,30]
print(sum(nums)) #合計
print(sum(nums)/len(nums)) #平均
