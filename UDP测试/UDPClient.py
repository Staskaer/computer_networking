from socket import *        # 形成网络通信的基础
serverName = '127.0.0.1'  # 设置服务器所在地址
serverPort = 12000  # 设置服务器套接字端口
clientSocket = socket(AF_INET, SOCK_DGRAM)
# 创建客户套接字，名称为clientSocket，AF_INET表示使用ivp4
# 第二个参数指明套接字类型，即UDP
message = input('Input local sentence :')  # 指示用户输入参数
clientSocket.sendto(message.encode(), (serverName, serverPort))
# encode将字符串转换为字节类型
# sendto为报文附上目的地址，并通过套接字发送
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
# 当因特网分组到达该套接字时，分组数据被放在modifiedMessage
# 源地址被放在serverAddress,包括主机名和端口号
print(modifiedMessage.decode())  # 解码并打印出来
clientSocket.close()  # 关闭套接字
