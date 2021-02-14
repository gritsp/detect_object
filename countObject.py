import cv2
import numpy as np
import os
import glob
from math import copysign, log10

class objectDetect():
    #input path image to crop icon card in center. This will save image cropped
    def createImgMatch(self,folderPath):
        listImg = glob.glob(folderPath+'/*.jpg')
        t = 0
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
                rect = cv2.minAreaRect(c)
                x,y,w,h = cv2.boundingRect(c)      
                print('x: '+str(x)+', y: '+str(y)+', h: '+str(h)+', w: '+str(w))
                if h/w>1 and h>20 and w>20:
                    x=x+int(w*0.24)
                    y=y+int(h*0.31)    
                    h = h-int(h*0.31*2)
                    w = w-int(w*0.24*2)
                    cv2.imwrite(str(t)+'.jpg',img[y:y+h, x:x+w])
                    print('x: '+str(x)+', y: '+str(y)+', h: '+str(h)+', w: '+str(w)+', t: '+str(t))
                    t+=1
                    
                elif w/h>1 and h>20 and w>20:
                    x=x+int(w*0.31)
                    y=y+int(h*0.24)
                    h = h-int(h*0.24*2) 
                    w = w-int(w*0.31*2)   
                    cv2.imwrite(str(t)+'.jpg',img[y:y+h, x:x+w])
                    print('x: '+str(x)+', y: '+str(y)+', h: '+str(h)+', w: '+str(w)+', t: '+str(t))
                    t+=1

    #input path image cropped. This medthod will return array of image
    def loadImgToList(self,plus,revert,stop):
        # plus = r'./newData/Plus/'
        # revert = r'./newData/Revert/'
        # stop = r'./newData/Stop/'
        # print(glob.glob(plus+'*.jpg'))
        # print(glob.glob(revert+'*.jpg'))
        # print(glob.glob(stop+'*.jpg'))
        # plus = glob.glob(plus+'*.jpg')
        
        plus = [cv2.imread(i,cv2.IMREAD_GRAYSCALE) for i in glob.glob(plus+'*.jpg')]
        stop =  [cv2.imread(i,cv2.IMREAD_GRAYSCALE) for i in glob.glob(stop+'*.jpg')]
        revert = [cv2.imread(i,cv2.IMREAD_GRAYSCALE) for i in glob.glob(revert+'*.jpg')]
        return [plus,revert,stop]
    

    #input frame or image. This medthod will return rectangel of center card detected to array and input text to img
    def createImg(self,img):
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        _,binary = cv2.threshold(img_gray,200,255,cv2.THRESH_BINARY)
        # cv2.imshow('bin',binary)
        cnts,_ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        imgList = []
        for i,c in enumerate(cnts):
            rect = cv2.minAreaRect(c) # return (x,y), (w,h), angle
            x,y,w,h = cv2.boundingRect(c)
            if h/w>1 and h>20 and w>20:
                x=x+int(w*0.24)
                y=y+int(h*0.31)    
                h = h-int(h*0.31*2)
                w = w-int(w*0.24*2)    
                imgList.append([binary[y:y+h, x:x+w],(y,x)]) 
                box = cv2.boxPoints(rect)
                box = np.intp(box) 
                cv2.drawContours(img, [box], 0, (0,255,0),2)
                
            elif w/h>1 and h>20 and w>20:
                x=x+int(w*0.31)
                y=y+int(h*0.24)
                h = h-int(h*0.24*2) 
                w = w-int(w*0.31*2)   

                imgList.append([binary[y:y+h, x:x+w],(y,x)]) 
                box = cv2.boxPoints(rect)
                box = np.intp(box) 
                cv2.drawContours(img, [box], 0, (0,255,0),2)
                
        return imgList,img
    

    #This will check matchshape of image input and data image and return obj matchshape and count obj
    def matchShape(self,imgList,dataList):
        ref = []
        count = [0,0,0]
        for i in imgList:
            img = i[0]
            temp = []
            for j in range(len(dataList)):
                for k in dataList[j]:
                    
                    _,kT=cv2.threshold(k,110,255,cv2.THRESH_BINARY)
                    ms = cv2.matchShapes(img,kT,cv2.CONTOURS_MATCH_I2,0)
                    if j==0:
                        if temp==[]:
                            temp = [ms,img,'Plus',i[1],kT]
                        else:
                            if ms<temp[0]:
                                temp = [ms,img,'Plus',i[1],kT]
                    elif j==1:
                        if temp==[]:
                            temp = [ms,img,'Revert',i[1],kT]
                        else:
                            if ms<temp[0]:
                                temp = [ms,img,'Revert',i[1],kT]
                    else:
                        if temp==[]:
                            temp = [ms,img,'Stop',i[1],kT]
                        else:
                            if ms<temp[0]:
                                temp = [ms,img,'Stop',i[1],kT]
            if temp[2]=='Plus':
                count[0]+=1
            elif temp[2]=='Revert':
                count[1]+=1
            elif temp[2]=='Stop':
                count[2]+=1


            ref.append(temp)
    
            
        return ref,count

    #This will put text shape of obj to img
    def showImg(self,img,imgMatch):
        for i in imgMatch:
            y,x = i[3]
            cv2.putText( img, i[2], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255) )
        
        return img