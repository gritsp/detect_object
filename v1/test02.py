import cv2
import numpy as np
import os
import glob

def createImgMatch():
    imgPath = './pics'
    listImg = glob.glob(imgPath+'/*.jpg')
    crop = []
    for i in listImg:
        img = cv2.imread(i)
        h,w,c = img.shape
        newWidth = 800
        newHight = newWidth*h//w
        img = cv2.resize(img,(newWidth,newHight),interpolation = cv2.INTER_AREA)
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        _,binary = cv2.threshold(img_gray,110,255,cv2.THRESH_BINARY)

        cnts, hier = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        
        for j,c in enumerate(cnts):
            rect = cv2.minAreaRect(c) # return (x,y), (w,h), angle 
            x,y,w,h = cv2.boundingRect(c)      
            x=x+w//4
            y=y+h//4               
            if h/w>1 or (1<w/h<1.6):
                crop.append(img[y:y+h-2*(h//4), x:x+w-2*(w//4)]) 
                
                # crop.append(binary[y:y+h, x:x+w]) 
                # box = cv2.boxPoints(rect)
                # box = np.intp(box) 
                # cv2.drawContours(img, [box], 0, (0,255,0),2)
                
    # try:
    for i in crop:
        cv2.imshow(str(crop.index(i)),i)
        cv2.imwrite(str(crop.index(i))+'.jpg',i)
    # except:
    #     pass

# cap = cv2.VideoCapture(1)
# imgPath = './crop'
# listImg = glob.glob(imgPath+'/*.jpg')
# # print(listImg)
# listImg = [cv2.cvtColor(cv2.imread(i),cv2.COLOR_BGR2GRAY) for i in listImg]
# while True:
#     _,frame = cap.read()
#     img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     ret,binary = cv2.threshold(img,150,255,cv2.THRESH_BINARY)

#     cnts, hier = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     crop = []
#     for _,c in enumerate(cnts):
#         rect = cv2.minAreaRect(c) # return (x,y), (w,h), angle 
#         x,y,w,h = cv2.boundingRect(c)       
        
#         if h/w>1 or (1<w/h<1.6):
#             crop.append(img[y:y+h, x:x+w])

#     ref = []
#     for k in crop:
#         for i in listImg:
#             ref.append([cv2.matchShapes(k,i,cv2.CONTOURS_MATCH_I3,0),listImg.index(i),crop.index(k)])
        
#     temp=0
#     res = ''
#     for i in ref:
#         # print(type(i[1]))
#         if i[0]>temp:
#             if i[1]==0 or i[1]==1:
#                 res = 'Plus'+str(i[2])
#             elif i[1]==2 or i[1]==3:
#                 res = 'Revert'+str(i[2])
#             elif i[1]==4 or i[1]==5:
#                 res = 'Stop'+str(i[2])
#             temp=i[0]
#     cv2.imshow('frame',frame)
#     print(res)
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         break
createImgMatch()    
# for i in listImg:
#     cv2.imshow(str(listImg.index(i)),i)
# cv2.waitKey(0)
cv2.destroyAllWindows()