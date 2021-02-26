# -*- conding: utf-8 -*-
# Author:ononok
# Time:2020/12/11
import socket
# 使用socket创建☝一个套接字
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('客户端链接服务器ip地址是:127.0.0.1端口号是:7799')
# 2 访问服务器
tcp_client_socket.connect(('127.0.0.1', 7799))

# 3 给服务器发送信息
tcp_client_socket.send('hello world'.encode())

# 关闭服务器
tcp_client_socket.close()
