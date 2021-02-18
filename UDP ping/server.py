# 使用随机数来模拟丢包
from socket import *
import random
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))  # 创建并绑定UDP套接字端口

while True:
    rand = random.randint(0, 10)  # 生成随机数
    message, address = serverSocket.recvfrom(1024)  # 收到客户端发送的信息
    message = message.upper()
    if rand < 4:
        continue
    serverSocket.sendto(message, address)  # 当满足条件则返回大写字符
