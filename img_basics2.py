import cv2
import numpy as np
black = np.zeros([100,80,3],'uint8')
cv2.imshow("black",black)
print(black[0,0,:])#frst pixel all the values

ones = np.ones([100,100,3],'uint8')
cv2.imshow('ones',ones)
print(ones[0,0,:])

white = np.ones([100,100,3],'uint8')#uint16 is not working
white *= (2**8-1)
cv2.imshow("white",white)
print(white[0,0,:])

color = ones.copy()
color[:,:] = (255,0,0)#bgr format
cv2.imshow('blue',color)
print(color[0,0,:])

cv2.waitKey(0)
cv2.destroyAllWindows()