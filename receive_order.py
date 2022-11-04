# encoding: utf-8
import socket
import time
import sys
# print("服务端开启")
# #套接字接口
# mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #设置IP和端口
# host = '183.173.70.4'
# port = 22
# #bind绑定该端口
# mySocket.bind((host, port))
# mySocket.listen(10)

file = open('order.txt', 'w')

def socket_service():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # IP地址留空默认是本机IP地址
        s.bind(('', 21))
        s.listen(7)
    except socket.error as msg:
        print(msg)
        sys.exit(1)

    while True:
        sock, addr = s.accept()
        msg = sock.recv(1024)
        string = msg.decode('utf-8')
        
        if string == 'Send Image Request!':
            with open('order.txt', 'r+') as file:
                print(file.readline())
                file.seek(0)
                file.truncate()
                print('1', file=file)
        else:
            # file.write('NOT_SEND')
            # print('NOT_SEND', file=file)
            # with open('order.txt', 'r+') as file:
            #     print(file.readline())
            #     file.seek(0)
            #     file.truncate()
            #     print('0', file=file)
            pass

        sock.close()
        time.sleep(0.01)
        # print(sock)

socket_service()


# while True:
#     #接收客户端连接
#     print("等待连接....")
#     client, address = mySocket.accept()
#     print("新连接")
#     print("IP is %s" % address[0])
#     print("port is %d\n" % address[1]) 
#     #读取消息
#     msg = client.recv(1024)
#     #把接收到的数据进行解码
#     print(msg.decode("utf-8"))
#     time.sleep(1)
    # print("读取完成")
    # if msg == b"hello":
    # print("你好，老弟")
    # if msg == b"qq":
    #     client.close()
    #     mySocket.close()
    #     print("程序结束\n")
    #     exit()
