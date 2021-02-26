import socket 

# 创建一个套接字
# socket.AF_INET ipv4 协议
# socket.SOCK_STREAM 
tcp_server_soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定一个端口，提供服务 只能被一个程序使用一个端口
tcp_server_soket.bind(("127.0.0.1", 7788))

# 监听客户端的信息
tcp_server_soket.listen()



# 接收客户端链接，如果有客户端链接过来了，返回客户端了链接对象与客户端的地址
# 服务器客户端的链接对象 可以进行数据的接收
# 阻塞信息 相当于input
client_socket, client_addr = tcp_server_soket.accept()
print("nihao")
client_socket.send("你好".encode())
# 接收信息
recv = client_socket.recv(1024)

print(recv)

# print(f'收到了来自{client_addr}的数据{recv.decode()}')

# 发送信息


# 先结束客户端与服务器的链接
client_socket.close()

# 再结束服务器提供服务的链接
tcp_server_soket.close()