import cv2
import numpy as np
import imutils   #now it's working :) ohk bbye.......

img = cv2.imread('C:\\Users\Hp\PycharmProjects\opencv\images\shapes.png',1)
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

image = img.copy()
index = -1
thickness = 4
color = (255,0,255)

#bad contour detection (if it is not rectangle then it is bad contour)
def bad_contours(c):
    #approximate the contour
    perimeter = cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c, 0.02 * perimeter, True)  # used to identify if a contour is square of not
    return not len(approx) == 4

cntr = cv2.findContours(gray.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cntr = imutils.grab_contours(cntr)
mask = np.ones(image.shape[:2],'uint8')*255

for c in cntr:
    if bad_contours(c):
        cv2.drawContours(mask,[c],-1,0,-1)

image = cv2.bitwise_and(image,image,mask=mask)
cv2.imshow('before',img)
cv2.imshow('after',image)
cv2.imshow('mask',mask)

cv2.waitKey(0)
cv2.destroyAllWindows()