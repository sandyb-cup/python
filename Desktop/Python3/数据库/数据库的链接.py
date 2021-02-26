import pymysql
conn = pymysql.connect(host="localhost",user="root",password="2913329720",charset="utf8") # 链接数据库
cur = conn.cursor() # 创建游标
comm = 'use china;'
answer = cur.execute(comm) # 游标指令
data = cur.fetchall() # 获取游标的所有信息
comm_data = 'select * from data;'
sulter = cur.execute(comm_data)
city_info = cur.fetchall()
for i in city_info:
    print(i[0])
conn.commit() # 提交数据
cur.close() # 游标关闭
conn.close() # 关闭链接


