# -*- conding: utf-8 -*-
# Author:ononok
# Time:2020/12/12
import threading
import time

def download(url, url_num=None):
    print(f"请求的url:{url},请求编号:{url_num}")
    time.sleep(1)
    print(f"结束的url:{url},结束编号:{url_num}")


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
'''
    多线程的运行机制是按照cup的运行机制来的
    
    如果想要多线程的输出也有一个循序 在执行多线程的时候加上一个处理就行(对执行的子进程进行编号)
'''

start_time = time.time()

for url in urls:
    # 对子进程进行编号处理
    url_num = int(int(url.split('=')[-1]) / 10)
    # 在进行args赋值得时候不要忘记加上一个(url,)的"，"_不然参数传递会报一个错误 参数混乱
    t1 = threading.Thread(target=download, args=(url,), kwargs={'url_num':url_num})

    t1.start()

while len(threading.enumerate())>1:
    '''
        单独给pass资源占有率会很高 所以加上一个延迟函数进行延迟    
    '''
    time.sleep(0.1)
    # pass

print('所有请求花费时间是:',time.time()-start_time)

'''
     默认情况下主线程会等子进程全部结束之后结束
     
'''