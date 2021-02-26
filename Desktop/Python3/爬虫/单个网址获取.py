import requests
import os
url = input("url:")
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
res = requests.get(url, headers=headers)
res_content = res.content
file_name = 'github_image'
image_name = input("name")
try:
    os.makedirs(file_name)
except FileExistsError:
    pass
with open(file_name+'/'+image_name+'.jpg','wb+') as file:
    file.write(res_content)

