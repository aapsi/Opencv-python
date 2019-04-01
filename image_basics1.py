import cv2
import numpy as np
img = cv2.imread("C:\\Users\Hp\PycharmProjects\opencv\OpenCV_Logo.png",0)
print(img)
print(len(img))#num of rows
print(len(img[0]))#num of columns
print(len(img[0][0]))#num of channels
print(img[10,5])#it will print all the values at the current pixel location
print(img.shape)#returns the properties of the image
cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()