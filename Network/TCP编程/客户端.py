# coding:utf-8

import socket

# 客户端：创建TCP连接时，主动发起请求的叫客户端
# 服务端：接收请求的

# 首先创建一个socket
# AF_INET 表示 IPV4 协议
# SOCK_STREAM 指定使用面向流的 TCP 协议
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 然后建立连接
# 参数是一个元组("www.sina.com.cn", 80)，第一个是网址或者IP，第二个是服务器暴露的端口
sk.connect(("www.sina.com.cn", 80))

sk.send(b"GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n")

# 等待接收数据
data = []
while True:
	# 每次接收1024字节的数据
	tempData = sk.recv(1024)
	if tempData:
		data.append(tempData)
	else:
		break

datStr = (b"".join(data)).decode("utf-8")

# 断开连接
sk.close()
print(datStr)

