import cv2
import numpy as np
import os
import glob
from math import copysign, log10

imgPath = './pics'
listImg = glob.glob(imgPath+'/*.jpg')
# for i in listImg:
img = cv2.imread('./pics/test01.jpg')
hight, width, chanel = img.shape
newWidth = 800
newHight = newWidth*hight//width
img = cv2.resize(img,(newWidth, newHight), interpolation = cv2.INTER_AREA)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,binary = cv2.threshold(img_gray,110,255,cv2.THRESH_BINARY)

moment = cv2.moments(binary)
huMoments = cv2.HuMoments(moment)

# print(i)
for i in range(0,7):
    huMoments[i] = -1*copysign(1.0,huMoments[i])*log10(abs(huMoments[i]))
    print("{:.5f}".format(huMoments[i][0]))

cnts, hier = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

minRect = [None]*len(cnts)

drawing = np.zeros(img.shape, np.uint8)
cv2.drawContours(drawing, cnts, -1, (255,255,255), -1)

crop = []
cv2.imshow("image", img)
for i,c in enumerate(cnts):
    minRect[i] = cv2.minAreaRect(c) # return (x,y), (w,h), angle 
    x,y,w,h = cv2.boundingRect(c)
    if h/w>1.4:
        crop.append(img[y:y+h, x:x+w])
        # box = cv2.boxPoints(minRect[i])
        # box = np.intp(box) 
        # cv2.drawContours(img, [box], 0, (0,255,0),2)
for i in crop:
    cv2.imshow('crop '+str(crop.index(i)),i)
cv2.imshow("image", img)
cv2.imshow("binary", binary)
cv2.imshow("drawing", drawing)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(0)