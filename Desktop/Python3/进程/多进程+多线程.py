# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
"""
    数据量大的时候 会更加趋向于理论值

    默认只用一条线程 100*1s = 100s
    十条线程 100/10 = 10
    十进程 + 十线程 100 / 10/ 10 *1s = 1s
"""
import concurrent.futures
import requests
import time
baidu_url = ['https://www.baidu.com/'] * 100
def process_pool(process_urls, process_name):
    # urls  100 个
    # 创建一个线程池
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executer:
        # process_urls 拆成十份
        for index, url in enumerate(process_urls):
            executer.submit(get_html, url, process_name, index)

def get_html(url, process_name, index):
    response = requests.get(url)
    print(process_name, index, response.url)

if __name__ == '__main__':
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executer:
        # 把任务拆分成十份
        for i in range(10):
            executer.submit(process_pool, baidu_url, "进程"+str(i+1))
    print(time.time() - start_time)