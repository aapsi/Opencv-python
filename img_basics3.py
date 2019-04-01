import cv2
import numpy as np

color = cv2.imread('C:\\Users\Hp\PycharmProjects\opencv\\640.jpg',1)
cv2.imshow('butterfly',color)
cv2.moveWindow('butterfly' ,0 ,0)
height,width,channels = color.shape
print(height)
print(width)
print(channels)

b,g,r = cv2.split(color)
bgr_split = np.concatenate((b,g,r),axis =1)
cv2.imshow('bgr split',bgr_split)
'''
color_split = np.empty([height,width*3,3],'uint8')
color_split[:,0:width] = cv2.merge([b,b,b])
color_split[:,width:width*2] = cv2.merge([g,g,g])
color_split[:,width*2:width*3] = cv2.merge([r,r,r])
cv2.imshow('channels',color_split)
cv2.moveWindow('channels',0,height)
'''
hsv = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
hsv_split = np.concatenate((h,s,v),axis = 1)
cv2.imshow('hsv split',hsv_split)


cv2.waitKey(0)
cv2.destroyAllWindows()