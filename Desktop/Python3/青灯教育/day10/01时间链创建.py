# -*- conding: utf-8 -*-
# author:Andy
# time:2020/7/29
"""
需求
    1 构建所有2019 1 1 到2010 1 1 日字符串时间链
    2 2019～1～1 - 2020～1～1
"""
import datetime
import pprint
star_time = datetime.date(2019,1,1)

stop_time = datetime.date(2020,1,1)

diffrent_date = datetime.timedelta(days=1)

now_time = star_time
date_list = []
while True:
    if star_time <= stop_time:
        # print(star_time)
        date_list.append(star_time)
        star_time += diffrent_date
    else:
        break

pprint.pprint(date_list)