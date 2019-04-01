import cv2
import numpy as np

cam = cv2.VideoCapture(0)
color = (0,255,0)
line_width = 2
radius = 50
point = (100,100)

def click(event,x,y,flags,param):
    global point,pressed
    if event == cv2.EVENT_LBUTTONUP:
        print('pressed',x,y)
        point = (x,y)

cv2.namedWindow('frame')
cv2.setMouseCallback('frame',click)

while(True):
    ret,frame = cam.read()
    frame = cv2.resize(frame,(0,0),fx = 0.5,fy = 0.5)
    cv2.circle(frame,point,radius,color,line_width)
    cv2.imshow('frame',frame)

    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

