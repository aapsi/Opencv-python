import cv2
import numpy as np

img = cv2.imread('C:\\Users\Hp\PycharmProjects\opencv\images\shapes.png',1)
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow('gray',gray)
#blur = cv2.GaussianBlur(gray,(5,5),0)

thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow('thresh',thresh)

contours , hierarchy = cv2.findContours(thresh , cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print('no. of contours is {}'.format(len(contours)))

image = img.copy()
index = -1
thickness = 4
color = (255,0,255)

objects = np.zeros([gray.shape[0],gray.shape[1],3],'uint8')
for c in contours:
    cv2.drawContours(objects,[c],-1,color,-1)
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c,True)
    M = cv2.moments(c)
    cx =int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cv2.circle(objects,(cx,cy),4,(255,255,255),-1)

    print('area = {} perimeter = {}'.format(area,perimeter))

cv2.imshow('contours',objects)
cv2.waitKey(0)
cv2.destroyAllWindows()