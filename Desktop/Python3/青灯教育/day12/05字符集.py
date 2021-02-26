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
# 如果长度超过12个，最多只会匹配到11个
# 但需要匹配. 字符的时候，可以转义一下
# \w a-z A-z 1-9
result = re.findall('\d{5,11}@\w+\.\w{2,3}', text)
# [0123456789] 等价于\d
# [a-zA-Z0-9] 等价于[/w]

# [1-9,d]
print(result)
print(re.findall('[\4ue00-\u9fa5]', text))
# 正则表达式的工作模式是匹配 Unicode码 二进制



# 数字 + 小写字母