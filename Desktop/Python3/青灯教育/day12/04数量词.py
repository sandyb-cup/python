# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import re
text = """
123453422@qq.com
122121323@qq.com
43435434@qq.com
1234454344545345453324345353234354
"""
# 如果长度超过12个，最多只会匹配到11个
# 但需要匹配. 字符的时候，可以转义一下
# \w a-z A-z 1-9
result = re.findall('\d{5,11}@\w+\.\w{2,3}', text)

print(result)

# 数字 + 小写字母