# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
import datetime

birth_day = datetime.datetime.strptime('1949-10-01',"%Y-%m-%d")

now_day = datetime.datetime.now()

diff_date = now_day - birth_day
print(diff_date)
print(diff_date.total_seconds())

