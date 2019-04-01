import cv2
import numpy as np
img = cv2.imread('C:\\Users\Hp\PycharmProjects\opencv\\640.jpg',1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray.jpg',gray)

b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]
rgba = cv2.merge((b, g, r, r))#how to change the img viewer
cv2.imwrite('rgba.png', rgba)
#cv2.imshow('picture', rgba)


cv2.waitKey(0)
cv2.destroyAllWindows()
