import cv2
import numpy as np
from math import copysign, log10

cap = cv2.VideoCapture(1)
ret, frame = cap.read()
img_draw = np.zeros(frame.shape)

while cap.isOpened():
    
    ret, frame = cap.read()
    img = frame
    # img = cv2.resize(img,(newWidth, newHight), interpolation = cv2.INTER_AREA)
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    ret,binary = cv2.threshold(img_gray,150,255,cv2.THRESH_BINARY)

    moment = cv2.moments(binary)
    huMoments = cv2.HuMoments(moment)

    # print(i)
    # for i in range(0,7):
    #     huMoments[i] = -1*copysign(1.0,huMoments[i])*log10(abs(huMoments[i]))
    #     print("{:.5f}".format(huMoments[i][0]))

    cnts, hier = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)



    drawing = np.zeros(img.shape, np.uint8)
    cv2.drawContours(drawing, cnts, -1, (255,255,255), -1)

    crop = []
    for i,c in enumerate(cnts):
        rect = cv2.minAreaRect(c) # return (x,y), (w,h), angle 
        x,y,w,h = cv2.boundingRect(c)
        x=x+w//4
        y=y+h//4
        if h/w>1 or (1<w/h<1.8):
            crop.append(img[y:y+h, x:x+w])
            box = cv2.boxPoints(rect)
            box = np.intp(box) 
            cv2.drawContours(img, [box], 0, (0,255,0),2)
    #     print(len(c))
    # h,w,c = [0,0,3]
    # for i in crop:
        # cH,cW,cC = i.shape
        # h+=cH
        # w+=cW
    # cropNew = np.zeros((h,w,3), np.uint8)
    # print(len(crop))
    try:
        
        # cv2.waitKey(30)
        # cv2.destroyAllWindows()        
        for i in crop:
            # iC = cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)

            # ret,bC = cv2.threshold(iC,150,255,cv2.THRESH_BINARY)
            cv2.imshow('new '+str(crop.index(i)),i)
    except:
        pass
    cv2.imshow("image", img)
    cv2.imshow("binary", binary)
    # cv2.imshow("drawing", drawing)
    

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
# cv2.waitKey(0)
