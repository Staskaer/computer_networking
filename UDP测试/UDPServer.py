from socket import *  # 形成网络通信的基础
serverPort = 12000  # 设定服务器端口号
serverSocket = socket(AF_INET, SOCK_DGRAM)
# 创建服务器套接字，名称为clientSocket，AF_INET表示使用ivp4
# 第二个参数指明套接字类型，即UDP
serverSocket.bind(('', serverPort))
# 将端口号与服务器套接字分配在一起
# 这是手动分配
print("the server is ready to receive")
while True:  # 该while循环允许无期限地等待接收分组并处理
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
