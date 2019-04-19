import cv2
import numpy as np

image = cv2.imread('C:\\Users\Hp\PycharmProjects\opencv\images\\faces.jpg',1)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
path = "C:\\Users\Hp\PycharmProjects\opencv\haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(path)

faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.50,minNeighbors= 5,minSize = (40,40))
print(len(faces))

for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
