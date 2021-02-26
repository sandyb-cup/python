import requests
from bs4 import BeautifulSoup
import os
import pprint
url = 'https://www.googletagservices.com/activeview/js/current/osd.js?cb=%2Fr20100101'
headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.3"}
res = requests.get(url, headers=headers, stream=True)
res_content = res.content
print(res_content)
file_name = input("请输入文件名字:")
os.makedirs(file_name)
video_path = file_name+'/bilibil.mp4'
with open(video_path, 'wb+') as file:
    file.write(res_content)


