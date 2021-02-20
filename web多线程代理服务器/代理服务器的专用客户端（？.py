from socket import *        # 形成网络通信的基础
serverName = '192.168.0.102'  # 设置服务器所在地址
serverPort = 11000  # 设置服务器套接字端口
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
# 执行三次握手，创建TCP连接
head = " HTTP/1.1\r\nHost: 192.168.0.102:12000\r\nConnection: keep-alive\r\nUser-Agent: Mozilla/5.0\r\n\r\n"
sentence = input('Input filename(including .html) : ')  # 输入
sentence = "GET /" + sentence + head
clientSocket.send(sentence.encode())  # 向服务器发送数据

responseHead = clientSocket.recv(1024).decode()
response = responseHead
while responseHead != "":  # 不断接受代理服务器发回的数据
    responseHead = clientSocket.recv(1024).decode()
    response = response + responseHead


print(response)
a = input("\n\n\n\ndone, please enter \'Enter\' to quit\n")
