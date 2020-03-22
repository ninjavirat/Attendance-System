import numpy as np
import cv2



cap = cv2.VideoCapture('/home/vishnu/Desktop/college_video.mp4')
# cap.set(1, 400)
# cap.set(1, 400)



# def change_res(width, height):

#     cap.set(3, width)
#     cap.set(4, height)


# change_res(400, 400)





while(cap.isOpened()):
  ret, frame = cap.read()
  resize = cv2.resize(frame, (640, 480)) 
  gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
  cv2.imshow('frame',gray)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
_
cap.release()
cv2.destroyAllWindows()
