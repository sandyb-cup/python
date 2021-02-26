import socket 

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_server_socket.bind(("127.0.0.1", 7788))

tcp_server_socket.listen()


# client_socker, client_addr = tcp_server_socket.accept()

tcp_server_socket.send("你好python".encode())

data = tcp_server_socket.recv(1024)
print(data.encode())
print(data)


# print

