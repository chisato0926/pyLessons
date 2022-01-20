import requests
from bs4 import BeautifulSoup

res=requests.get('https://joytas.net/kaba/')
res.encoding=res.apparent_encoding
#第1引数にhtml文字列,第2引数にパーサーを指定する。今回は追加ライブラリ不要な'html.parser'を指定
soup=BeautifulSoup(res.text,'html.parser')

#BeautifulSoupオブジェクトをprintにそのまま渡すと全文を表示する
#print(soup)

#タグで取得
ele=soup.find('title')
#textコンテント表示
print(ele.text)

#要素を結果セット(ResultSet)として取得
imgs=soup.find_all('img')
for img in imgs:
    #属性にアクセスするにはgetメソッドを使う
    print(img.get('src'))

#その他の要素の取得方法

#idを指定
div=soup.find(id='headerImageBox')

#classで取得
imgs=soup.select('.headerImage')
for img in imgs:
    print(img.get('src'))

#カバの名前取得
names=soup.select('td:first-child')
for name in names:
    print(name.text)

#li要素中のa全取得
links=soup.select('li a')
#ファイル書き込み
with open('zoo.txt','w',encoding='utf-8') as file:
    for link in links:
        file.write(f'{link.text}:{link.get("href")}\n')
