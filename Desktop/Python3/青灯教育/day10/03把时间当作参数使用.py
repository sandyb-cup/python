# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import requests
import time

def get_html(url):
    response = requests.get(url)
    return response.text

def save_html(html, name):
    with open(name, mode='w', encoding='utf-8') as f:
        f.write(html)
start_time = time.time()
html_contents = get_html('http://www.baidu.com')
print(f'请求html花了{time.time()-start_time}秒')

save_time = time.time()
save_html(html_contents, 'baidu.txt')
print(f'保存文件花了{time.time()-save_time}秒')
"""
    请求网页花了多长时间 保存文件花了多长时间
"""