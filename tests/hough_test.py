import cv2
import numpy as np 
import sys
import pytesseract
from PIL import Image
from matplotlib import pyplot as plt



filename = 'traff2.jpg';

img = cv2.imread(filename);
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17,17 )
cv2.imshow('gray',gray)


edges = cv2.Canny(gray, 150, 170);
cv2.imshow('edge', edges);

### contours finder

(_, cnts, _) = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
screenCnt = None

for c in cnts:
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	
	if len(approx) == 4:
	#if len(approx) < 9:
		screenCnt = approx
		break

#screenCnt = cv2.convexHull(screenCnt)
cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)
cv2.imshow("traffic", img)


### hough detection
'''
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow('hough img', img)
'''


cv2.waitKey(0)
cv2.destroyAllWindows()
