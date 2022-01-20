def funcA(z):
    ans=z*2 #ans=z*aを修正
    print(ans)

def funcB(x,y):
    z=x+y
    funcA(z)

x=10
y=20
funcB(10,20)


print('hello') #print('hello)を修正


try:
    price=int(input('料金＞＞'))
    number=int(input('人数＞＞'))
    print(f'1人{price/number}円')
except:
    print('料金または人数は整数で入力')
finally:
    print('ok')
print('終了')

