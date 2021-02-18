from socket import *
import time
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
serverSocket.settimeout(20)  # 设置timeout

num_last = 0


def report(difference, num):  # 此函数将未收到的数据包列出
    i = 1
    while i < difference:
        nub = int(num) + i
        print("NO." + str(nub) + " missing")
        i += 1


while True:
    try:
        message, address = serverSocket.recvfrom(1024)
        message = message.decode()

        num = message.split()[0]  # 获取序列号
        difference = int(num) - int(num_last)

        if difference == 1:  # 序列号连续
            print("NO."+str(num) + " received, the client is on line")
        else:  # 序列号不连续，说明有丢包
            report(difference, num_last)
            print("NO."+str(num) + " received, the client is on line")

        if difference > 3:  # 当数据包出现连续丢失超过3个
            print("the client is off line for a few secs")

        num_last = num

    except Exception as e:  # timeout
        print("the client is off line \n")
        break

serverSocket.close()
