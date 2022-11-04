import socket
import sys
import os
import struct

# def get_image(img_path='imgs/one_camera/', idx=0):
#     img_name = img_path + f'{idx}.jpg'
#     os.system('fswebcam --no-banner -r 640x480 ' + img_name)
#     # os.system(f'raspistill -o {img_name} -t 20')
#     # print(time.time())
#     return img_name

def socket_service_data():
    
    filepath = '/home/pi/DianZiSheJi/imgs/one_camera/0.jpg'
    
    # 连接
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('', 24))  # 在不同主机或者同一主机的不同系统下使用实际ip
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print("Wait for Connection..................")
    sock, addr = s.accept()
    
    while True:
        # 收
        buf = sock.recv(BUFSIZ)  # 接收数据
        print(buf)
        buf1 = buf.decode('utf-8')  # 解码
        print(buf1)
        if not buf:
            break
        print('Received message:', buf1)
        # return buf
        # 发
        if buf1 == '1':
            print('开始传图......')
            fhead = struct.pack(b'128sl', bytes(os.path.basename(filepath), encoding='utf-8'), os.stat(filepath).st_size)
            s.send(fhead)
            print('client filepath: {0}'.format(filepath))
    
            fp = open(filepath, 'rb')
            while 1:
                data = fp.read(1024)
                if not data:
                    print('{0} 发送成功...'.format(filepath))
                    break
                s.send(data)
        
        # buf = input("input data:")  # 输入要传输的数据
        # if not buf:
        #     break
        # sock.send(buf.encode())  # 将要传输的数据编码发送，如果是字符数据就必须要编码发送
        
    # 关闭socket
    sock.close()


if __name__ == '__main__':
    # 初始化
    # name = socket.gethostname()
    # HOST = socket.gethostbyname(name)  # 获取阿里云服务器私网IP，使用ifconfig可查询
    HOST = '183.173.62.252'
    PORT = 137
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    socket_service_data()