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

def wapper_get_html(*args,**kwargs):
    start_time = time.time()
    reponse = requests.get(*args,**kwargs).text
    stop_time = time.time()
    # 使用一个函数 对旧的函数进行封装
    print(f'请求所花时间{stop_time - start_time}')

    return reponse

def wapper_save_html(*args,**kwargs):
    start_time = time.time()
    save_html(*args,**kwargs)
    stop_time = time.time()
    # 使用一个函数 对旧的函数进行封装
    print(f'请求所花时间{stop_time - start_time}')

# html_text = wapper_get_html(url = 'http://www.baidu.com')
# wapper_save_html(html_text, 'baidu.html')


def time_wapper(fun, *args,**kwargs):
    start_time = time.time()
    print(*args)
    print(**kwargs)

    reponse = fun(*args, **kwargs)
    stop_time = time.time()
    return reponse
    # 使用一个函数 对旧的函数进行封装
    # print(f'请求所花时间{stop_time - start_time}')
html_text = time_wapper(wapper_get_html, 'http://www.baidu.com')

time_wapper(wapper_save_html,html_text,'baidu2.html')


