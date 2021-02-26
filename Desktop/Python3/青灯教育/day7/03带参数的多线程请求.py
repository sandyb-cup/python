# -*- conding: utf-8 -*-
# Author:ononok
# Time:2020/12/12
import threading
import time

def download(url, url_num = None):
    print(url_num)
    print('请求：',url)
    time.sleep(0.3)
    print('结束:', url)


urls = [
    'https://maoyan.com/board/4?offset=0',
    'https://maoyan.com/board/4?offset=10',
    'https://maoyan.com/board/4?offset=20',
    'https://maoyan.com/board/4?offset=30',
    'https://maoyan.com/board/4?offset=40',
    'https://maoyan.com/board/4?offset=50',
    'https://maoyan.com/board/4?offset=60',
    'https://maoyan.com/board/4?offset=70',
    'https://maoyan.com/board/4?offset=80',
    'https://maoyan.com/board/4?offset=90',
]
start_time = time.time()

for url in urls:

    t1 = threading.Thread(target=download, args=(url,), kwargs={'url_num': url.split('=')[-1]})
    t1.start()

while len(threading.enumerate())>1:
    pass

print('所有请求花费时间是:',time.time()-start_time)
