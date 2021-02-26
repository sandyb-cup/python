# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import re
text = """
123453422@qq.com
122121323@qq.com
43435434@qq.com
1234454344545345453324345353234354
你好 世界

"""

# 有些想要匹配的数据换行了
# .* 匹配跨行的内容，默认情况下无法匹配
# re.s 把换行的变得让，进行匹配 不加re.s 只能在一行内容里面进行匹配
# ？是非贪婪模式 只要后面有内容匹配就停止运行
result = re.findall('(.*?)@qq.com', text)
print(result)

