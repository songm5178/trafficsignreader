import cv2
import numpy as np 
import sys
import pytesseract
import math
from PIL import Image
from matplotlib import pyplot as plt




filename = '../morphed_mask.png';

img = cv2.imread(filename);
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17,17 )
#cv2.imshow('gray',gray)


edges = cv2.Canny(gray, 150, 170);
cv2.imshow('edge', edges);


minLineLength = 3
maxLineGap = 250
lines = cv2.HoughLinesP(edges,1,np.pi/180,10,minLineLength,maxLineGap)

# for i in range(len(lines)):
# 	for x1,y1,x2,y2 in lines[i]:
#     	cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
#     	print lines[i]

for i in range(len(lines)):
	# print lines[i]
	# print lines[i][0]
	for x1,y1,x2,y2 in lines[i]:
		cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)





cv2.imshow('hough img', img)

print lines[0]
print len(lines)


cv2.waitKey(0)
cv2.destroyAllWindows()