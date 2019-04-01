import cv2
import numpy as np
img = cv2.imread('C:\\Users\Hp\PycharmProjects\opencv\hairface-thresh-b.jpg',1)
img = cv2.resize(img,(400,550))
cv2.imshow('original',img)

kernel = np.ones((5,5),'uint8')

dilate = cv2.dilate(img,kernel,iterations =1)
cv2.imshow('dilate',dilate)

erode = cv2.erode(img,kernel,iterations = 1)
cv2.imshow('erode',erode)

cv2.waitKey(0)
cv2.destroyAllWindows()
