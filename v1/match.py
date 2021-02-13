import cv2
import numpy as np
from math import copysign, log10

showLog = True

ref = cv2.imread(r"E:\My Drive\NU\Courses\Computer Vision\OpenCV\test images\Hu\C0.png",cv2.IMREAD_GRAYSCALE) 

A0 = cv2.imread(r"E:\My Drive\NU\Courses\Computer Vision\OpenCV\test images\Hu\A0.png",cv2.IMREAD_GRAYSCALE) 
A1 = cv2.imread(r"E:\My Drive\NU\Courses\Computer Vision\OpenCV\test images\Hu\A1.png",cv2.IMREAD_GRAYSCALE)
A2 = cv2.imread(r"E:\My Drive\NU\Courses\Computer Vision\OpenCV\test images\Hu\A2.png",cv2.IMREAD_GRAYSCALE)
A3 = cv2.imread(r"E:\My Drive\NU\Courses\Computer Vision\OpenCV\test images\Hu\A3.png",cv2.IMREAD_GRAYSCALE)
A4 = cv2.imread(r"E:\My Drive\NU\Courses\Computer Vision\OpenCV\test images\Hu\A4.png",cv2.IMREAD_GRAYSCALE)
A5 = cv2.imread(r"E:\My Drive\NU\Courses\Computer Vision\OpenCV\test images\Hu\A5.png",cv2.IMREAD_GRAYSCALE)

C0 = cv2.imread(r"E:\My Drive\NU\Courses\Computer Vision\OpenCV\test images\Hu\C0.png",cv2.IMREAD_GRAYSCALE)
C1 = cv2.imread(r"E:\My Drive\NU\Courses\Computer Vision\OpenCV\test images\Hu\C1.png",cv2.IMREAD_GRAYSCALE)
C2 = cv2.imread(r"E:\My Drive\NU\Courses\Computer Vision\OpenCV\test images\Hu\C2.png",cv2.IMREAD_GRAYSCALE)
C3 = cv2.imread(r"E:\My Drive\NU\Courses\Computer Vision\OpenCV\test images\Hu\C3.png",cv2.IMREAD_GRAYSCALE)
C4 = cv2.imread(r"E:\My Drive\NU\Courses\Computer Vision\OpenCV\test images\Hu\C4.png",cv2.IMREAD_GRAYSCALE)
C5 = cv2.imread(r"E:\My Drive\NU\Courses\Computer Vision\OpenCV\test images\Hu\C5.png",cv2.IMREAD_GRAYSCALE)


mA0 = cv2.matchShapes(ref,A0,cv2.CONTOURS_MATCH_I3,0)
mA1 = cv2.matchShapes(ref,A1,cv2.CONTOURS_MATCH_I3,0)
mA2 = cv2.matchShapes(ref,A2,cv2.CONTOURS_MATCH_I3,0)
mA3 = cv2.matchShapes(ref,A3,cv2.CONTOURS_MATCH_I3,0)
mA4 = cv2.matchShapes(ref,A4,cv2.CONTOURS_MATCH_I3,0)
mA5 = cv2.matchShapes(ref,A5,cv2.CONTOURS_MATCH_I3,0)

mC0 = cv2.matchShapes(ref,C0,cv2.CONTOURS_MATCH_I3,0)
mC1 = cv2.matchShapes(ref,C1,cv2.CONTOURS_MATCH_I3,0)
mC2 = cv2.matchShapes(ref,C2,cv2.CONTOURS_MATCH_I3,0)
mC3 = cv2.matchShapes(ref,C3,cv2.CONTOURS_MATCH_I3,0)
mC4 = cv2.matchShapes(ref,C4,cv2.CONTOURS_MATCH_I3,0)
mC5 = cv2.matchShapes(ref,C5,cv2.CONTOURS_MATCH_I3,0)
 
print("Shape Distances Between \n-------------------------")
print("ref and A0 : {}".format(mA0))
print("ref and A1 : {}".format(mA1))
print("ref and A2 : {}".format(mA2))
print("ref and A3 : {}".format(mA3))
print("ref and A4 : {}".format(mA4))
print("ref and A5 : {}".format(mA5))
print("ref and C0 : {}".format(mC0))
print("ref and C1 : {}".format(mC1))
print("ref and C2 : {}".format(mC2))
print("ref and C3 : {}".format(mC3))
print("ref and C4 : {}".format(mC4))
print("ref and C5 : {}".format(mC5))