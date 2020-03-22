import urllib.request
import cv2
import numpy as np


# import cv2

# cap = cv2.VideoCapture(0)

# def make_1080p():
#     cap.set(3, 1920)
#     cap.set(4, 1080)

# def make_720p():
#     cap.set(3, 1280)
#     cap.set(4, 720)

# def make_480p():
#     cap.set(3, 640)
#     cap.set(4, 480)

# def change_res(width, height):
#     cap.set(3, width)
#     cap.set(4, height)

# make_720p()
# change_res(1280, 720)



# #url='http://192.168.0.11:80/shot1.png'
# url = 'http://192.168.43.134:8080/shot1.png'


# def login_page(user_name, password):
# 	pass



	
cap = cv2.VideoCapture('http://192.168.0.14/doc/page/preview.asp' , 0)
def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)


def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)

make_720p()
change_res(1280, 720)

while True:
    ret , frame = cap.read()
    #cv2.rectangle(frame , (100,100) , (200,200) , [255,0,0],2)
    cv2.imshow("capture" , frame)


    if ord('q')==cv2.waitKey(10):
        exit(0)

# user_name = 'admin'
# password = 'admin'
# #login_page(user_name, password)

cap.release()
cv2.destroyAllWindows()