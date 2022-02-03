import turtle
t=turtle.Turtle() # インスタンス作成
t.shape('turtle') # 見た目を亀に
for i in range(4):
    t.forward(100) #向いている方向に100移動
    t.right(90) #90度回転
    t.forward(100)
turtle.mainloop() # 実行を監視
