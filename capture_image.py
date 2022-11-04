import os
import sys
import re
import time

# import cv2
# a = cv2.imread('imgs/one_camera/8.jpg')

# # import ipdb; ipdb.set_trace()

# from picamera import PiCamera

img_path = 'imgs/fast/'

# for i in range(20):
#     img_name = img_path + f'{i}.jpg'
#     os.system('fswebcam --no-banner -r 640x480 ' + img_name)
#     # os.system(f'raspistill -o {img_name} -t 20')
#     print(time.time())

import cv2
cap = cv2.VideoCapture(0)
flag = cap.isOpened()

while (flag):
    ret, frame = cap.read()
    print(time.time())
    # cv2.imwrite(img_path + 'a.jpg', frame)
    # cv2.imshow("Capture_Paizhao", frame)
    # print('a')
    # k = cv2.waitKey(1) & 0xFF
    # if k == ord('s'):  # 按下s键，进入下面的保存图片操作
    #     cv2.imwrite(img_path + str(index) + ".jpg", frame)
    #     print("save" + str(index) + ".jpg successfuly!")
    #     print("-------------------------")
    #     index += 1
    # elif k == ord('q'):  # 按下q键，程序退出
    #     break
cap.release() # 释放摄像头
cv2.destroyAllWindows()# 释放并销毁窗口
