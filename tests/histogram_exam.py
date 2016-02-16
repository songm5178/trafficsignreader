import cv2
import numpy as np 
import sys
import pytesseract
import math
from PIL import Image
from matplotlib import pyplot as plt


filename = 'traff3.jpg'

img = cv2.imread(filename)

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow('gray', gray)
cv2.imwrite('gray.jpg', gray)
print '11111111111'
message = pytesseract.image_to_string(Image.open('gray.jpg'))
print message


#gray = cv2.bilateralFilter(gray, 11, 17,17 )
equ = cv2.equalizeHist(gray)
cv2.imwrite('equ.jpg', equ)
print '2222222222'
message = pytesseract.image_to_string(Image.open('equ.jpg'))
print message


cv2.imshow('equ', equ)

cv2.waitKey(0)
cv2.destroyAllWindows()