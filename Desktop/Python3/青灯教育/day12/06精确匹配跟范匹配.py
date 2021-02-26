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

# 括号
# 把邮箱分成三个部分， 一个字符串@邮箱类型，域名类型
result = re.findall("(\w+)@(\w+)\.(com)", text)
print(result)
