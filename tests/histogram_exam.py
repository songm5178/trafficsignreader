import cv2
import numpy as np 
import sys
import pytesseract
import math
from PIL import Image
from matplotlib import pyplot as plt


filename = 'DSC_0723.JPG'

img = cv2.imread(filename)
cv2.imshow('ori', img)

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow('gray', gray)
cv2.imwrite('gray.jpg', gray)
oedges = cv2.Canny(gray, 150, 170);
cv2.imwrite('Oedge.jpg', oedges);




#gray = cv2.bilateralFilter(gray, 11, 17,17 )
equ = cv2.equalizeHist(gray)
cv2.imshow('equ', equ)
cv2.imwrite('equ.jpg', equ)
hedges = cv2.Canny(equ, 150, 170);
cv2.imshow('Hedge', hedges)
cv2.imwrite('Hedge.jpg', hedges);




cv2.waitKey(0)
cv2.destroyAllWindows()