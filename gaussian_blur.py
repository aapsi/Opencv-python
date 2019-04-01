import cv2
import numpy as np
img = cv2.imread('C:\\Users\Hp\PycharmProjects\opencv\hairface-thresh-b.jpg',1)
img = cv2.resize(img,(400,550))
cv2.imshow('original',img)

blur = cv2.GaussianBlur(img,(5,15),0)#only odd numbers in tuple
cv2.imshow('blur',blur)

cv2.waitKey(0)
cv2.destroyAllWindows()