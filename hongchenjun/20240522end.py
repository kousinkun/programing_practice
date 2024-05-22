import requests
from bs4 import BeautifulSoup
import datetime
import os
def listup(url):
    # html取得
    response = requests.get(url)
    response.encoding = 'utf-8'
    print(response.text)
    l = url.split('/')
    today = datetime.date.today()
    dirname = today.strftime('%Y%m%d')
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    fullpath = os.path.join(dirname, l[-1])
    #"20240522"+"/"+ "sample"
    with open(fullpath, 'w', encoding='utf-8', newline='') as f:
        f.write(response.text)

    # html解析
    soup = BeautifulSoup(response.text, 'html.parser')
    for a_tag in soup.find_all('a'):
        text = a_tag.string
        href = a_tag.get('href')
        print(href)
        listup(href)



url = 'https://secure.winschool.jp/sozai/IT56/chapter13/sample13_3_2.html'
listup(url)
