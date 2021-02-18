from socket import *  # 形成网络通信的基础
serverPort = 12000  # 设定服务器端口号
serverSocket = socket(AF_INET, SOCK_STREAM)
# 创建服务器套接字，名称为clientSocket，AF_INET表示使用ivp4
# 第二个参数指明套接字类型，即TCP
serverSocket.bind(('', serverPort))  # 将端口号与服务器套接字分配在一起
serverSocket.listen(2)  # 让服务器聆听来自客户的TCP请求，括号中为最大连接数
print("this server is ready to receive\n")
while True:
    connectionSocket, add = serverSocket.accept()
    # 当客户敲门时，调用accept（）方法，创建一个新的套接字，由特定客户专用
    # 客户与服务器完成了握手，创建一个TCP连接。
    # 服务器与客户之间可以借助此连接互相发送数据
    # 一方发出的所有字节能确保到达另一方，且保证顺序
    sentence = connectionSocket.recv(1024).decode()  # 接受数据
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())  # 发送处理完成的数据
    connectionSocket.close()
