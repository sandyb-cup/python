import schedule
import time
import threading
def job():
    print('program excute')
name = 'zhangxin'
schedule.every(10).seconds.do(job)
while True:
    schedule.run_pending()

# schedule.every(10).minute.do(job,name)
# # 每十分钟运行任务
# schedule.every(1).hour.do(job, name)
# # 每一个小时运行任务
# schedule.every().day.at("10:30").do(job)
# # 每天10:30 运行任务
# schedule.every(5).to(10).days.do(job)
# # 5 到 10 天运行任务
# schedule.every().monday.do(job)
# # 每周星期一运行任务
# schedule.every().wednesday.at("14:15").do(job)
# # 每周三运行任务
