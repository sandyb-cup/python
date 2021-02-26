# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import sys
code_path = '../../魔法函数/02new.py'
# path环境包的导入顺序

sys.path.insert(0, code_path)
for path in sys.path:
    print(path)
