import cv2
import numpy as np

img = cv2.imshow("C:\\Users\Hp\PycharmProjects\opencv\hairface-thresh-b.jpg",1)
img = cv2.imshow("C:\\Users\Hp\PycharmProjects\opencv\(_resize(_1759.jpg",1)
#resize
img_half = cv2.resize(img ,(0,0),fx = 0.5,fy = 0.5 )
img_stretch = cv2.resize(img,(600,600))
img_stretch_near = cv2.resize(img,(600,600),interpolation=cv2.INTER_NEAREST)

cv2.imshow('half',img_half)
cv2.imshow('stretch',img_stretch)
cv2.imshow('near',img_stretch_near)


#rotation
M = cv2.getRotationMatrix2D((0,0),-90,1)
img_rotate = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))


cv2.waitKey(0)
cv2.destroyAllWindows()