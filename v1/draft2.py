import cv2
import numpy as np
import os
import glob



def createImgMatch(folderPath):
    listImg = glob.glob(folderPath+'/*.jpg')
    # crop = []
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
            # cv2.imshow('cnt',img)
            # cv2.waitKey(0)
            # print(y)        
            print('x: '+str(x)+', y: '+str(y)+', h: '+str(h)+', w: '+str(w))
            if h/w>1 and h>20 and w>20:
                # x=x+int(w*1.4)
                # y=y+int(h*2.7)     
                # print('x: '+str(x)+', y: '+str(y)+', h: '+str(h)+', w: '+str(w))
                x=x+int(w*0.24)
                y=y+int(h*0.31)    
                h = h-int(h*0.31*2)
                w = w-int(w*0.24*2)
                # cv2.imshow('img',img[y:y+h-int(h*2.7), x:x+w-int(w*1.4)])
                # crop.append(img[y:y+h-2*(h//4), x:x+w-2*(w//4)])
                cv2.imwrite(str(t)+'.jpg',img[y:y+h, x:x+w])
                # cv2.imwrite(str(t)+'.jpg',(img[y:y+h, x:x+w]))
                print('x: '+str(x)+', y: '+str(y)+', h: '+str(h)+', w: '+str(w)+', t: '+str(t))
                t+=1
                
            elif w/h>1 and h>20 and w>20:
                
                # x=x+int(w*1.4)
                # y=y+int(h*2.7)     
                # print('x: '+str(x)+', y: '+str(y)+', h: '+str(h)+', w: '+str(w))
                x=x+int(w*0.31)
                y=y+int(h*0.24)
                h = h-int(h*0.24*2) 
                w = w-int(w*0.31*2)   
                # cv2.imshow('img',img[y:y+h-int(h*1.4), x:x+w-int(w*2.7)])
                # crop.append(img[y:y+h-2*(h//4), x:x+w-2*(w//4)])
                cv2.imwrite(str(t)+'.jpg',img[y:y+h, x:x+w])
                # cv2.imwrite(str(t)+'.jpg',(img[y:y+h, x:x+w]))
                print('x: '+str(x)+', y: '+str(y)+', h: '+str(h)+', w: '+str(w)+', t: '+str(t))
                t+=1

    # for i in crop:
    #     # cv2.imshow(str(crop.index(i)),i)
    #     cv2.imwrite(str(crop.index(i))+'.jpg',i) 

def loadImgToList():
    plus = r'./newData/Plus/'
    revert = r'./newData/Revert/'
    stop = r'./newData/Stop/'
    print(glob.glob(plus+'*.jpg'))
    print(glob.glob(revert+'*.jpg'))
    print(glob.glob(stop+'*.jpg'))
    # plus = glob.glob(plus+'*.jpg')
    
    plus = [cv2.imread(i,cv2.IMREAD_GRAYSCALE) for i in glob.glob(plus+'*.jpg')]
    stop =  [cv2.imread(i,cv2.IMREAD_GRAYSCALE) for i in glob.glob(stop+'*.jpg')]
    revert = [cv2.imread(i,cv2.IMREAD_GRAYSCALE) for i in glob.glob(revert+'*.jpg')]
    return [plus,revert,stop]

    
def createImg(img):
    h,w,c = img.shape
    newWidth = 800
    newHight = newWidth*h//w
    img = cv2.resize(img,(newWidth,newHight),interpolation = cv2.INTER_AREA)
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _,binary = cv2.threshold(img_gray,160,255,cv2.THRESH_BINARY)
    cv2.imshow('bin',binary)
    cnts,_ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    imgList = []
    for i,c in enumerate(cnts):
        rect = cv2.minAreaRect(c) # return (x,y), (w,h), angle
        x,y,w,h = cv2.boundingRect(c)
        # x=x+w//4
        # y=y+h//4               
        # if h/w>1.6 or (w/h<1.6):
        #     imgList.append([binary[y:y+h-2*(h//4), x:x+w-2*(w//4)],(y,x)]) 
        #     # imgList.append([binary[y:y+h, x:x+w],(y,x)]) 
        #     box = cv2.boxPoints(rect)
        #     box = np.intp(box) 
        #     # cv2.putText( img, str(cnts.index(c)), (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255) )
        #     cv2.drawContours(img, [box], 0, (0,255,0),2)
        if h/w>1 and h>20 and w>20:
            # x=x+int(w*1.4)
            # y=y+int(h*2.7)     
            # print('x: '+str(x)+', y: '+str(y)+', h: '+str(h)+', w: '+str(w))
            x=x+int(w*0.24)
            y=y+int(h*0.31)    
            h = h-int(h*0.31*2)
            w = w-int(w*0.24*2)    
            # crop.append(img[y:y+h-2*(h//4), x:x+w-2*(w//4)])
            # cv2.imwrite(str(t)+'.jpg',(img[y:y+h-h*2.7, x:x+w-w*1.4]))

            imgList.append([binary[y:y+h, x:x+w],(y,x)]) 
            # imgList.append([binary[y:y+h, x:x+w],(y,x)]) 
            box = cv2.boxPoints(rect)
            box = np.intp(box) 
            # cv2.putText( img, str(cnts.index(c)), (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255) )
            cv2.drawContours(img, [box], 0, (0,255,0),2)
            
        elif w/h>1 and h>20 and w>20:
                
            # x=x+int(w*1.4)
            # y=y+int(h*2.7)     
            # print('x: '+str(x)+', y: '+str(y)+', h: '+str(h)+', w: '+str(w))
            x=x+int(w*0.31)
            y=y+int(h*0.24)
            h = h-int(h*0.24*2) 
            w = w-int(w*0.31*2)     
            # crop.append(img[y:y+h-2*(h//4), x:x+w-2*(w//4)])
            # cv2.imwrite(str(t)+'.jpg',(img[y:y+h-h*1.4, x:x+w-w*2.7]))

            imgList.append([binary[y:y+h, x:x+w],(y,x)]) 
            # imgList.append([binary[y:y+h, x:x+w],(y,x)]) 
            box = cv2.boxPoints(rect)
            box = np.intp(box) 
            # cv2.putText( img, str(cnts.index(c)), (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255) )
            cv2.drawContours(img, [box], 0, (0,255,0),2)
            
    return imgList,img

def matchShapes(imgList,dataList):
    ref = []
    count = [0,0,0]
    for i in imgList:
        # img = cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
        img = i[0]
        temp = []
        for j in range(len(dataList)):
            for k in dataList[j]:
                
                _,kT=cv2.threshold(k,110,255,cv2.THRESH_BINARY)
                ms = cv2.matchShapes(img,kT,cv2.CONTOURS_MATCH_I2,0)
                # print(str(ms)+' '+str(j))
                if j==0:
                    if temp==[]:
                        temp = [ms,img,'Plus',i[1],kT]
                        # print(str(temp[0])+' Plus')
                    else:
                        if ms<temp[0]:
                            temp = [ms,img,'Plus',i[1],kT]
                            # print(str(temp[0])+' Plus')
                elif j==1:
                    if temp==[]:
                        temp = [ms,img,'Revert',i[1],kT]
                        # print(str(temp[0])+' Revert')
                    else:
                        if ms<temp[0]:
                            temp = [ms,img,'Revert',i[1],kT]
                            # print(str(temp[0])+' Revert')
                else:
                    if temp==[]:
                        temp = [ms,img,'Stop',i[1],kT]
                        # print(str(temp[0])+' Stop')
                    else:
                        if ms<temp[0]:
                            temp = [ms,img,'Stop',i[1],kT]
                            # print(str(temp[0])+' Stop')
        if temp[2]=='Plus':
            count[0]+=1
        elif temp[2]=='Revert':
            count[1]+=1
        elif temp[2]=='Stop':
            count[2]+=1


        ref.append(temp)
   
        
    return ref,count

def showImg(img,imgMatch):
    for i in imgMatch:
        y,x = i[3]
        cv2.putText( img, i[2], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255) )
        # cv2.imshow(str(i[0]),i[4])
    return img

# createImgMatch('./picData')
# def main():
cap =cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

data = loadImgToList()
# print(data)
while True:
    _,img = cap.read()
    cv2.imshow('frame',img)
# img = cv2.imread(r"./picTest/test1.jpg")
    try:
        imgList,img = createImg(img)

        # print(len(imgList))
        imgMatch,count = matchShapes(imgList,data)
        img = showImg(img,imgMatch)
        # print(count)
        cv2.putText( img, 'Plus: '+str(count[0])+', Revert: '+str(count[1])+', Stop: '+str(count[2]), (0,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255) )
        cv2.imshow('img',img)
    except:
        cv2.imshow('img',img)
        # pass
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
# cv2.waitKey(0)


# if __name__=='__main__':
#     main()