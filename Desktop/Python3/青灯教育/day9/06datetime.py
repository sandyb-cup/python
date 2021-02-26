# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
# date 日期 年月日
# time 时间 时分秒
import datetime

today = datetime.datetime.today()

# 一百天以前是星期几
print(today)

# 时间差对象
one_day = datetime.timedelta(days =1)

# 时间差对象
old_day = today - one_day * 100
print(old_day)

