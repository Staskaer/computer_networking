from socket import *        # 形成网络通信的基础
serverName = '127.0.0.1'  # 设置服务器所在地址
serverPort = 12000  # 设置服务器套接字端口
clientSocket = socket(AF_INET, SOCK_STREAM)
# 创建客户套接字，名称为clientSocket，AF_INET表示使用ivp4
# 第二个参数指明套接字类型，即TCP
clientSocket.connect((serverName, serverPort))
# 执行三次握手，创建TCP连接
sentence = input('Input lowercase sentence : ')  # 输入
clientSocket.send(sentence.encode())  # 向服务器发送数据
modifiedSentence = clientSocket.recv(1024)  # 接受服务器返回数据
print('From server : ' + modifiedSentence.decode())  # 打印返回数据
clientSocket.close()  # 关闭套接字
