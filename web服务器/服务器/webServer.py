from socket import *  # 形成网络通信的基础
serverSocket = socket(AF_INET, SOCK_STREAM)  # 创建客户套接字
serverPort = 12000  # 设置服务器套接字端口
serverSocket.bind(("", serverPort))  # 将端口号与服务器套接字分配在一起
serverSocket.listen(2)  # 让服务器聆听来自客户的TCP请求，括号中为最大连接数
while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  # 接受来自客户端数据
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]  # 分割来获得请求文件名
        path = r"D:/vs_code_files/python/projects/网络/web服务器/服务器/" + \
            str(filename[1:])
        with open(path, 'r')as f:
            outputdata = f.read()
        #打开请求的文件#
        header = ' HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (
            len(outputdata))
        connectionSocket.send(header.encode())  # 发送http头
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())  # 发送html页面
        connectionSocket.close()
    except IOError:  # 文件不存在
        header = ' HTTP/1.1 404 Found'
        connectionSocket.send(header.encode())  # 404报错
        connectionSocket.close()
serverSocket.close()
