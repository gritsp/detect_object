import cv2
from countObject import objectDetect

def main():
    #set video
    cap =cv2.VideoCapture(1)
    cap.set(3, 1280)
    cap.set(4, 720)

    #take class
    obj = objectDetect()

    #create image for take matchshape from path
    # obj.createImgMatch('./picData')

    #load image after crop from obj.createImgMacth
    data = obj.loadImgToList('./newData/Plus/','./newData/Revert/','./newData/Stop/')

    while True:
        _,img = cap.read()
        
        try:
            #call createImg
            imgList,img = obj.createImg(img)

            #call matchshape
            imgMatch,count = obj.matchShape(imgList,data)

            #call showImg
            img = obj.showImg(img,imgMatch)
            
            #put count obj to img
            cv2.putText( img, 'Plus: '+str(count[0])+', Revert: '+str(count[1])+', Stop: '+str(count[2]), (0,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255) )
            cv2.imshow('img',img)
        except:
            cv2.imshow('img',img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

if __name__=='__main__':
    main()