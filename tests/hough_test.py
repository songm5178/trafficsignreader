import cv2
import numpy as np 
import sys
import pytesseract
from PIL import Image
from matplotlib import pyplot as plt



filename = 'traff3.jpg';

img = cv2.imread(filename);
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray = cv2.bilateralFilter(gray, 9, 19, 50)
cv2.imshow('gray',gray)


edges = cv2.Canny(gray, 150, 200);
cv2.imshow('edge', edges);

(_, cnts, _) = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
screenCnt = None

for c in cnts:
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	
	if len(approx) == 4:
		screenCnt = approx
		break
        
print [screenCnt]



smallest = 99999
smallestIndex = 0
smaller = 99999
smallerIndex = 0
for i in range(0, 4):
    if screenCnt[i][0][0] < smallest:
        smaller = smallest
        smallerIndex = smallestIndex
        smallest = screenCnt[i][0][0]
        smallestIndex = i
    elif screenCnt[i][0][0] > smallest and screenCnt[i][0][0] < smaller:
        smaller = screenCnt[i][0][0]
        smallerIndex = i
left = []
left.append(smallestIndex)
left.append(smallerIndex)

smallest = 99999
smallestIndex = 0
smaller = 99999
smallerIndex = 0
for i in range(0, 4):
    if screenCnt[i][0][1] < smallest:
        smaller = smallest
        smallerIndex = smallestIndex
        smallest = screenCnt[i][0][1]
        smallestIndex = i
    elif screenCnt[i][0][1] > smallest and screenCnt[i][0][1] < smaller:
        smaller = screenCnt[i][0][1]
        smallerIndex = i
top = []
top.append(smallestIndex)
top.append(smallerIndex)

leftTop = 0
leftBottom = 0
rightTop = 0
rightBottom = 0
for i in range(0, 4):
    if i in left:
        if i in top:
            leftTop = i
        else:
            leftBottom = i
    else:
        if i in top:
            rightTop = i
        else:
            rightBottom = i
print left
print top
print screenCnt[leftTop]
print screenCnt[leftBottom]
print screenCnt[rightTop]
print screenCnt[rightBottom]

cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)
cv2.imshow("traffic", img)


cv2.waitKey(0)
cv2.destroyAllWindows()
