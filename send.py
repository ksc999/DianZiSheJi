import socket
import os
import sys
import struct
import time


def get_image(img_path='imgs/one_camera/', idx=0):
    img_name = img_path + f'{i}.jpg'
    os.system('fswebcam --no-banner -r 640x480 ' + img_name)
    # os.system(f'raspistill -o {img_name} -t 20')
    # print(time.time())
    return img_name


PC_ip = '183.173.63.234'
PC_port = 136

def sock_client(filepath):
    try:
        print('a')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('a')
        # 192.168.199.1和8088分别为服务端（pc）的IP地址和网络端口
        s.connect((PC_ip, PC_port))
    except socket.error as msg:
        print(msg)
        print(sys.exit(1))
    print('a')
    
    while True:
        # filepath是要被发送图片的路径
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
        s.close()
        break
        
        # time.sleep(2)
        # i = i + 1
        # if i == 10:
        #     s.close()
        #     break

import cv2
cap = cv2.VideoCapture(0)
flag = cap.isOpened()
img_path = 'imgs/fast/'

if __name__ == '__main__':
    root_path = 'imgs/one_camera/'
    i = 0
    while True:
        with open('order.txt', 'r+') as file:
            line = file.readline()
            if line == '1\n':
                print('start sending image')
                ret, frame = cap.read()
                filepath = img_path + f'{i}.jpg'
                cv2.imwrite(filepath, frame)
                # filepath = get_image(idx=i)
                # filepath = root_path + f'{i}.jpg'
                sock_client(filepath=filepath)
                file.seek(0)
                print('0', file=file)
                i += 1

