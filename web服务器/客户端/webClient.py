from socket import *        # 形成网络通信的基础
from bs4 import BeautifulSoup
serverName = '192.168.0.102'  # 设置服务器所在地址
serverPort = 12000  # 设置服务器套接字端口
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
# 执行三次握手，创建TCP连接
head = " HTTP/1.1\r\nHost: 127.0.0.1:12000\r\nConnection: keep-alive\r\nUser-Agent: Mozilla/5.0\r\n\r\n"
sentence = input('Input filename(including .html) : ')  # 输入
sentence = "GET /" + sentence + head
clientSocket.send(sentence.encode())  # 向服务器发送数据
responseHead = clientSocket.recv(1024).decode()
response = responseHead.split("\n", 2)[2]  # 获取信息
code = str(responseHead.split()[1]) + ' ' + \
    str(responseHead.split()[2])  # 获取状态码
soup = BeautifulSoup(response, 'html.parser')
print("status : " + code)
print("title : " + soup.title.string)
print("contenes : " + soup.body.get_text())

a = input("\n\n\n\ndone, please enter \'Enter\' to quit\n")
