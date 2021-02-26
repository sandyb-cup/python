# -*- conding: utf-8 -*-
# Author:ononok
# Time:2021/2/10
import requests
import json
from bs4 import BeautifulSoup
url = 'https://accounts.douban.com/j/mobile/login/basic'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}
data = {
    'remember': 'true',
    'name': '18279797380',
    'password': '$99991106$',
}
# session能自动保持cookies 后面就不需要使用cookies
session = requests.Session()
res = session.post(url=url,headers=headers,data=data)

cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
print(type(cookies_dict))
# 将字典转换成字符串
dict_str = json.dumps(cookies_dict)
print(type(dict_str))
# 将str转换成字典
str_dir = json.loads(dict_str)
print(type(str_dir))
# 将字典转换成cookies
cookies_type = requests.utils.cookiejar_from_dict(str_dir)
print(cookies_type)




