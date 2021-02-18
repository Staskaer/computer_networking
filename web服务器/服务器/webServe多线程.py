from socket import *  # 形成网络通信的基础
import threading
import os


def Server(tcpClisock, addr):  # 自定义线程函数

    BUFSIZE = 1024
    print('Waiting for the connection：', addr)
    data = tcpClisock.recv(BUFSIZE).decode()
    filename = data.split()[1]
    filename = filename[1:]

    if filename == "":  # 当未收到请求的文件
        tcpClisock.close()
        print("请输入要访问的文件")

    base_dir = r'D:\\vs_code_files\\python\\projects\\网络\\web服务器\\服务器'  # 设置服务器的初始路径
    file_dir = os.path.join(base_dir, filename)  # 设置文件路径

    if os.path.exists(file_dir):    # 当访问的文件在本地服务器存在时执行
        f = open(file_dir, encoding='utf-8')
        SUCCESS_PAGE = "HTTP/1.1 200 OK\r\n\r\n" + f.read()
        print(SUCCESS_PAGE)
        tcpClisock.sendall(SUCCESS_PAGE.encode())
        tcpClisock.close()
    else:  # 未找到所请求的文件
        FAIL_PAGE = "HTTP/1.1 404 NotFound\r\n\r\n" + \
            open(os.path.join(base_dir, "fail.html"), encoding="utf-8").read()
        print(FAIL_PAGE)
        tcpClisock.sendall(FAIL_PAGE.encode())
        tcpClisock.close()


if __name__ == '__main__':  # 主函数

    ADDR = ("", 12000)  # 分配IP、端口、创建套接字对象
    tcpSersock = socket(AF_INET, SOCK_STREAM)
    tcpSersock.bind(ADDR)
    tcpSersock.listen(5)
    print("waiting for connection......\n")
    while True:
        tcpClisock, addr = tcpSersock.accept()
        thread = threading.Thread(target=Server, args=(tcpClisock, addr))
        thread.start()
    tcpSersock.close()
