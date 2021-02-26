# -*- conding: utf-8 -*-
# Author:ononok
# Time:2020/12/11
import socket
# 创建一个socket对象
tcp_serve_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定一个ip地址 与端口提供服务
tcp_serve_socket.bind(('127.0.0.1', 7799))
print('ip地址:127.0.0.1','端口号为7799\n服务器启动开始....')

# 监听等待客户端请求， tcp_serve_socket相当于前台
# 128是接收信息的最大字节数
tcp_serve_socket.listen(128)

# 等待客户端请求 返回一个socket链接 客户端信息
# client_socket 是进行数据通信的链接
clilent_socket, client_addr = tcp_serve_socket.accept()
print(clilent_socket, client_addr)

# 服务器于客户端的数据进行交互
# 接收链接


recv_data = clilent_socket.recv(1024)
clilent_socket.send('(来自服务器)'.encode())
# 关闭客户端于服务器的链接
clilent_socket.close()

# 关闭服务器, 不再提供服务
tcp_serve_socket.close()