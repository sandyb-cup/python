import requests
from bs4 import BeautifulSoup
import json
import os
def get_urls(): # 获取短视频的url函数
    video_urls = []
    video_num = input("请问要多少页短视频:")
    for i in range(int(video_num)): # 请求循环
        url = 'https://v.6.cn/minivideo/getMiniVideoList.php?' # 原url地址
        # parameter参数
        parameter = {
            'act': 'recommend',
            'page': int(i),
            'pagesize': 20,
            }
        # 请求头
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
            }
        # 发起请求
        res = requests.get(url, headers=headers, params=parameter)
        res_json = res.json()
        # 解析请求
        json_content = res_json['content']['list']
        for datas in json_content:
            url = datas['playurl']
            video_urls.append(url)
            # 获取url
    return video_urls,headers
def video_clawer(): # 定义视频获取函数
    
    file_name = input('请输入你文件夹的名称:')
    os.makedirs(file_name) # 创建文件夹
    video_num = 0
    video_urls,headers = get_urls()
    for url in video_urls:
        video_num+=1
        # 获取请求
        res = requests.get(url, headers= headers)
        res_content = res.content
        with open(file_name+'/short_video'+str(video_num)+'.mp4','wb+') as file:
            # 写入文件
            file.write(res_content)
def main():
    video_clawer()
if __name__=='__main__':
    main()
        