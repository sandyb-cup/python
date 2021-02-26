# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
class File:
    def __init__(self, filename, mode ="w", encoding="utf-8"):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
    def __enter__(self):
        self.f = open('hello.text', mode='w', encoding='utf-8')
        print('进入文件')
        return self.f
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
        print('退出了上下文环境')
# 当进入环境的时候
with File('hello.text',mode = 'w', encoding='utf-8') as f:
    content = f.write('hello python')
