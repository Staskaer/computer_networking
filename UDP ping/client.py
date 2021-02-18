from socket import *
import time
serverName = '192.168.0.102'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

success = 0
err = 0
lst = []

for i in range(0, 10):
    sendTime = time.time()
    message = ('Ping %d %s' % (i+1, sendTime)).encode()
    try:
        clientSocket.sendto(message, (serverName, serverPort))
        returnedMessage, addr = clientSocket.recvfrom(1024)
        rtt = time.time() - sendTime
        lst.append(rtt)
        print('Sequence %d: Reply from %s    RTT = %.3fs' %
              (i+1, serverName, rtt))
        success += 1
    except Exception as e:
        print('Sequence %d: Request timed out' % (i+1))
        err += 1
clientSocket.close()
print("max = "+str(max(lst))+" min = "+str(min(lst)))
print("average = " + str(sum(lst)/len(lst)))
print("total = 10 " + "success = "+str(success))
print("lose rate = " + str(err/10))
