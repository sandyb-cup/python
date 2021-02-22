# -*- conding: utf-8 -*-
# Author:ononok
# Time:2021/2/10
import requests,re,os
from os import system
from bs4 import BeautifulSoup
import time

def join_content(content):
    results = ''.join(content)
    return results
headers = {
    'referer': 'https://movie.douban.com/subject/26342391/?from=showing',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
data = {
    'remember': 'true',
    'name': '18279797380',
    'password': '$99991106$',
}
url = 'https://movie.douban.com/'
res = requests.post(headers = headers,url = url, data=data)
# 获取登入cookies
cookies = res.cookies
res_text = res.text
soup = BeautifulSoup(res_text,'html.parser')
poster = soup.find_all('li',class_='poster')
try:
    os.mkdir('css实战/豆瓣简介')
except FileExistsError:
    system('rm -rf 豆瓣简介')
    os.mkdir('css实战/豆瓣简介')
for p in poster:
    a = p.find('a')
    url = re.findall('="(.*?)" onclick',str(a))
    name = re.findall('[\u4e00-\u9fa5]',str(a))
    time.sleep(0.5)
    res_content = requests.get(headers=headers,url =''.join(url),cookies = cookies)
    res_text = res_content.text
    soup = BeautifulSoup(res_text,'html.parser')
    indent = soup.find_all('div',id='link-report')
    content = re.findall('[\u4e00-\u9fa5]',str(indent))
    name = join_content(name)
    print(name)
    content = join_content(content)
    with open(f'css实战/豆瓣简介/{name}.text', 'w') as f:
        f.write(content)




