class Hero:
    def __init__(self,name,hp): #コンストラクタ
        self.name=name
        self.hp=hp
    def sleep(self,hours): #メソッド
        print(f'{self.name}は{hours}時間寝た')
        self.hp+=hours

print('スッキリファンタジー')
h=Hero('松田',100)
h.sleep(3)
print(f'{h.name}のHPは現在{h.hp}です')
