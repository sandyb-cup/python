# -*- conding: utf-8 -*-
# Author:ononok
# Time:2021/2/12
import requests
import os
from os import system
url = 'https://www.runoob.com/images/pic_bulboff.gif'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}
img_name = input('img_name:')
img_type = input('img_type:')
try:
    os.mkdir('images')
except FileExistsError:
    pass
res = requests.get(url=url, headers=headers)
res_content = res.content
with open(f'images/{img_name}.{img_type}','wb') as f:
    f.write(res_content)