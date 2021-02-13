import cv2
import numpy as np
import os
import glob
from math import copysign, log10

folderPath = './crop2/'
listImg = glob.glob(folderPath+'*.jpg')
print(listImg)

listImg = [cv2.imread(i,cv2.IMREAD_GRAYSCALE) for i in listImg]
# listImg = []
# for i in listImgOld:
    
#     _,binary = cv2.threshold(i,110,255,cv2.THRESH_BINARY)
#     listImg.append(binary)

img = './test1.jpg'
img = cv2.imread(img)
h,w,c = img.shape
newWidth = 800
newHight = newWidth*h//w
img = cv2.resize(img,(newWidth,newHight),interpolation = cv2.INTER_AREA)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,binary = cv2.threshold(img_gray,110,255,cv2.THRESH_BINARY)
cnts,_ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
crop = []
for i,c in enumerate(cnts):
    rect = cv2.minAreaRect(c) # return (x,y), (w,h), angle
    x,y,w,h = cv2.boundingRect(c)
    x=x+w//4
    y=y+h//4               
    if h/w>1 or (1<w/h<1.6):
        crop.append(img[y:y+h-2*(h//4), x:x+w-2*(w//4)]) 
        # crop.append(img[y:y+h, x:x+w]) 
        box = cv2.boxPoints(rect)
        box = np.intp(box) 
        cv2.drawContours(img, [box], 0, (0,255,0),2)

# moment = cv2.moments(binary)
# huMoments = cv2.HuMoments(moment)

# # print(i)
# for i in range(0,7):
#     huMoments[i] = -1*copysign(1.0,huMoments[i])*log10(abs(huMoments[i]))
#     print("{:.5f}".format(huMoments[i][0]))

ref = []
for i in crop:
    i = cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)

    print('---I---')
    moment = cv2.moments(i)
    huMoments = cv2.HuMoments(moment)

    # print(i)
    for k in range(0,7):
        huMoments[k] = -1*copysign(1.0,huMoments[k])*log10(abs(huMoments[k]))
        print("{:.5f}".format(huMoments[k][0]))
    temp = []
    for j in listImg:     
        moment = cv2.moments(j)
        huMoments = cv2.HuMoments(moment)

        print('---j---')
        for k in range(0,7):
            huMoments[k] = -1*copysign(1.0,huMoments[k])*log10(abs(huMoments[k]))
            print("{:.5f}".format(huMoments[k][0]))   

        x = cv2.matchShapes(i,j,cv2.CONTOURS_MATCH_I3,0)
        print('\n'+str(x)+', '+str(listImg.index(j)))
        if temp == []:
            temp = [x,i,j]
        else:
            # print(str(temp[0])+'test')
            if x<temp[0]:
                temp = [x,i,j]
    ref.append(temp)
    # mA0 = cv2.matchShapes(ref,A0,cv2.CONTOURS_MATCH_I3,0)
temp=0

for i in ref:
    print(str(i[0]))
    cv2.imshow(str(1+i[0]),i[1])
    
    cv2.imshow(str(listImg.index(i[2])+i[0]),i[2])




cv2.imshow('img',img)
cv2.waitKey(0)