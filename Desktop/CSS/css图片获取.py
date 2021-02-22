# -*- conding: utf-8 -*-
# Author:ononok
# Time:2021/1/25
import requests
from bs4 import BeautifulSoup
images_name = input('请输入图片名字:')
headers ={
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}
url='https://static.runoob.com/images/mix/searchicon.png'
res = requests.get(url=url, headers=headers)
res_content = res.content
with open(f'/Users/sandy/Desktop/CSS/css实战/images/{images_name}'+'.jpg','wb') as file:
    file.write(res_content)
