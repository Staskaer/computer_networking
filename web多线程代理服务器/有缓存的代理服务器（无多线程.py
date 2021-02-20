from socket import *

# 创建socket，绑定到端口，开始监听
tcpSerPort = 11000
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(('', tcpSerPort))
tcpSerSock.listen(5)
connestabilish = "HTTP/1.1 200 Connection Established\r\n\r\n"

while True:
    # 开始从客户端接收请求
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from: ', addr)
    message = tcpCliSock.recv(4096).decode()
    ifconnestablish = message.split()[0]

    if ifconnestablish == "CONNECT":  # 判断是不是CONNECT，目前此代理服务器无法处理此方法，尚待研究
        tcpCliSock.sendall(connestabilish.encode())  # 返回一个“知道了”就结束，无实际作用
        print("connection established")
        continue

    # 从请求中解析出filename
    filename = message.split()[1].replace("http://", "", 1).split("/")[1:][0]
    filename = "D:\\vs_code_files\python\projects\网络\web多线程代理服务器\缓存\\" + filename
    fileExist = "false"
    try:
        # 检查缓存中是否存在该文件
        with open(filename, "r")as f:
            outputdata = f.readlines()
        fileExist = "true"
        print('File Exists!')

        # 缓存中存在该文件，把它向客户端发送
        for i in range(0, len(outputdata)):
            tcpCliSock.send(outputdata[i].encode())
        print('Read from cache')

    # 缓存中不存在该文件，异常处理
    except IOError:
        print('File Exist: ', fileExist)
        if fileExist == "false":
            # 在代理服务器上创建一个tcp socket
            print('Creating socket on proxyserver')
            c = socket(AF_INET, SOCK_STREAM)

            try:  # 解析出主机地址和端口
                hostn = message.split()[4].split(":")[0]
            except:
                hostn = message.split()[4]
            try:
                port = int(message.split()[4].split(":")[1])
            except:
                port = 80

            try:
                c.connect((hostn, port))
                print('Socket connected to the host')
                c.sendall(message.encode())
                buff = c.recv(4096)
                tcpCliSock.sendall(buff)  # 将请求到的文件发回客户端

                tmpFile = open(filename, "w")  # 缓存
                tmpFile.writelines(buff.decode())  # .replace('\r\n', '\n'))
                tmpFile.close()
            except:
                print("Illegal request")  # 异常请求，非法处理

        else:
            print('File Not Found...Stupid Andy')
    tcpCliSock.close()
tcpSerSock.close()
