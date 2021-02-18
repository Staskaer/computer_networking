# 使用随机数来模拟丢包
from socket import *
import random
import time
serverName = '192.168.0.102'
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)  # UDP
i = 0

while True:
    i += 1
    rand = random.randint(0, 10)  # 生成随机数
    if rand < 4:
        print(str(i)+" passed")
        time.sleep(3)
        continue
    sendTime = time.time()
    message = ('%d %s' % (i, sendTime)).encode()
    print(str(i)+" sended")
    serverSocket.sendto(message, (serverName, serverPort))
    time.sleep(3)  # 每隔一秒发送一次
serverSocket.close()
