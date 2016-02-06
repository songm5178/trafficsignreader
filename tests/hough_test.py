import cv2
import numpy as np 
import sys
import pytesseract
from PIL import Image
from matplotlib import pyplot as plt



filename = 'traff3.jpg';

img = cv2.imread(filename);
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow('grat',gray)


edges = cv2.Canny(gray, 150, 170);
cv2.imshow('edge', edges);
'''
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()'''


cv2.waitKey(0)
cv2.destroyAllWindows()
