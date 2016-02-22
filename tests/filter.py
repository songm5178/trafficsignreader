import numpy as np 
import cv2
import sys
import pytesseract
import math
from PIL import Image
from matplotlib import pyplot as plt




filename = 'IMG_3467.jpg';

img = cv2.imread(filename);
cv2.imshow('ori', img);
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imwrite('gray.jpg', img)
edges = cv2.Canny(img, 150, 170)
cv2.imshow('Oedge', edges)
cv2.imwrite('edges.jpg', edges)




gaussian = cv2.GaussianBlur(img, (11,11), 0)
cv2.imshow('gaussian',gaussian)
cv2.imwrite('gaussian.jpg', gaussian)


bilateral = cv2.bilateralFilter(img, 11, 17,17 )
cv2.imshow('bilateral',bilateral)
cv2.imwrite('bilateral.jpg',bilateral)

gedges = cv2.Canny(gaussian, 150, 170);
cv2.imshow('Gedge', gedges);
cv2.imwrite('g_edges.jpg',gedges)

bedges = cv2.Canny(bilateral, 150, 170);
cv2.imshow('Bedge', bedges);
cv2.imwrite('b_edges.jpg',bedges)






cv2.waitKey(0)
cv2.destroyAllWindows()