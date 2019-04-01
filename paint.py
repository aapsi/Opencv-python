import cv2
import numpy as np

brush = cv2.imread('brush_r1.png',3)
eraser = cv2.imread('eraser1.png',3)
plus = cv2.imread('plus.png',3)
minus = cv2.imread('minus.png',3)
canvas = np.ones([1000,1000,3],'uint8')*255
canvas[0:30,0:1000] = (0,0,0)

color = (0,0,0)
line_width = -1
radius = 5
point = (100,100)
size = 0
pressed = False
erased = False
brushed = False
canvas[0:20,0:20] = brush
canvas[0:20,40:60] = eraser
canvas[0:20,80:100] = (0,0,255) #red color
canvas[0:20,120:140] = (255,0,0)#blue color
canvas[0:20,160:180] = (0,255,0)#green color
canvas[0:20,200:220] = plus
canvas[0:20,240:260] = minus

def click(event,x,y,flags,param):
    global point,pressed,color,erased,radius,brushed,size

    if event == cv2.EVENT_LBUTTONDOWN:
        if y in range(0,20) and x in range(0,20):
            brushed = np.invert(brushed)
            erased = False
                #cv2.circle(canvas, (x,y), radius, color, line_width)
                #canvas[y:y+2,x:x+2] = (0,0,255)
        if y in range(0,20) and x in range(40,60):
            erased = np.invert(erased)
            brushed = False

        if y in range(0,20) and x in range(80,100):
            color = (0,0,255)
        if y in range(0,20) and x in range(120,140):
            color = (255,0,0)
        if y in range(0,20) and x in range(160,180):
            color = (0,255,0)
        if y in range(0,20) and x in range(200,220):
            size += 3
        if y in range(0,20) and x in range(240,260):
            if size >0:
                size -= 3
            else:
                size = size

    if y in range(50, 1001):
        if brushed == True:
            if event == cv2.EVENT_LBUTTONDOWN:
                pressed = True
                cv2.circle(canvas, (x,y), radius + size, color, line_width)
                    #canvas[y:y + size, x:x + size] = (0, 0, 255)
            if event == cv2.EVENT_MOUSEMOVE and pressed:
                cv2.circle(canvas, (x,y), radius + size, color, line_width)
                #canvas[y:y +5, x:x +5] = (0, 0, 255)
            if event == cv2.EVENT_LBUTTONUP:
                pressed = False

        if erased == True:
            color1 = (255,255,255)
            if event == cv2.EVENT_LBUTTONDOWN:
                pressed = True
                cv2.circle(canvas, (x,y), radius+size, color1, line_width)

            elif event == cv2.EVENT_MOUSEMOVE and pressed == True:
                cv2.circle(canvas, (x, y), radius+size, color1, line_width)
            elif event == cv2.EVENT_LBUTTONUP:
                pressed = False

cv2.namedWindow('frame')
cv2.setMouseCallback('frame',click)

while(True):
    cv2.imshow("frame",canvas)
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
