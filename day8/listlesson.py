import pprint
data=list()
for i in range(10):
    temp=list()
    for j in range(10):
        temp.append(0)
    data.append(temp)
print(data)
pprint.pprint(data)

w=10
h=10
data=[None]*h
for i in range(h):
    data[i]=[0]*w
pprint.pprint(data)

#シャローコピー(shallow copy)
data=[[0]*w]*h
pprint.pprint(data)

#シャローコピーを書き換えた場合
data[1][1]=5
pprint.pprint(data)

#内包表記
data=[[0]*w for i in range(h)]
pprint.pprint(data)

#確認問題
for i in range(h):
    temp=[None]*w
    for j in range(w):
        temp[j]=i*10+j+1
    data[i]=temp
pprint.pprint(data)
#内包表記ver
data=[[i*10+j for j in range(1,11)] for i in range(0,10)]
pprint.pprint(data)


#1~7の要素を持つリスト
x=[i for i in range(1,8)]
print(x)

#1~7の要素の2乗した値を持つリスト
x=[i**2 for i in range(1,8)]
print(x)

#1~7の要素のうち偶数のリクエスト
x=[i for i in range(1,8) if i%2==0]
x=[i for i in range(2,7,2)]#ステップ
print(x)

#入れ子のforでリスト
x=[i*10+j for i in range(1,3) for j in range(2,5)]
print(x)

#2次元リスト
x=[[i*10+j for j in range(7,10)] for i in range(1,3)]
print(x)

#単位行列
row=col=3
matrix=[[1 if i==j else 0 for j in range(col)] for i in range(row)]
print(matrix)
