import cv2
from countObject import objectDetect

def main():
    cap =cv2.VideoCapture(1)
    cap.set(3, 1280)
    cap.set(4, 720)

    obj = objectDetect()
    # obj.createImgMatch('./picData')
    data = obj.loadImgToList('./newData/Plus/','./newData/Revert/','./newData/Stop/')
    while True:
        _,img = cap.read()
        
        try:
            imgList,img = obj.createImg(img)

        
            imgMatch,count = obj.matchShapes(imgList,data)
            img = obj.showImg(img,imgMatch)
            
            cv2.putText( img, 'Plus: '+str(count[0])+', Revert: '+str(count[1])+', Stop: '+str(count[2]), (0,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255) )
            cv2.imshow('img',img)
        except:
            cv2.imshow('img',img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

if __name__=='__main__':
    main()