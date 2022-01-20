import requests
from bs4 import BeautifulSoup
#フォルダ操作モジュール
from pathlib import Path
#url操作モジュール
import urllib
#時間操作モジュール
import time

load_url='https://joytas.net/kaba/'
res=requests.get(load_url)
res.encoding=res.apparent_encoding
soup=BeautifulSoup(res.text,'html.parser')

#フォルダ作成
out_folder=Path('downloaded')
out_folder.mkdir(exist_ok=True)
imgs=soup.select('#headerImageBox img')
for img in imgs:
    src=img.get('src')
    #絶対urlに変換
    img_url=urllib.parse.urljoin(load_url,src)
    #画像ロード
    loaded_img=requests.get(img_url)
    #ファイル名取得
    file_name=img.get('src').split('/')[-1]
    #保存画像パス
    out_path=out_folder.joinpath(file_name)
    with open(out_path,'wb') as file:
        file.write(loaded_img.content)
    time.sleep(1)
