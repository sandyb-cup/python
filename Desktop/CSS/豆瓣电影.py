# -*- conding: utf-8 -*-
# Author:ononok
# Time:2021/2/9
import requests
from bs4 import BeautifulSoup
import re,os
url = 'https://movie.douban.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}
res = requests.get(headers=headers,url=url)
res_text = res.text

soup = BeautifulSoup(res_text,'html.parser')
ul = soup.find_all('ul')
for p in ul:
    alt = p.find('img')
    print(alt)
    if alt:
        name = re.findall('[\u4e00-\u9fa5]',str(alt))
        url=''.join(re.findall('https://img'+'\d'+'.doubanio.com/view/photo/s_ratio_poster/public/p'+'\d*'+'.jpg',str(alt)))
        if url:
            re_img = requests.get(headers=headers,url=url)
            re_content = re_img.content
            with open('豆瓣电影图片/{}.jpg'.format(''.join(name)),'wb') as f:
                f.write(re_content)








