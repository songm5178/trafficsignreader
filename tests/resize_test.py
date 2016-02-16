import numpy as np
import cv2
from PIL import Image
import pytesseract
import sys
from matplotlib import pyplot as plt


filename = './DSC_0709.JPG'

img = cv2.imread(filename)
# cv2.imshow('ori', img)

resize = cv2.resize(img, None, fx = 0.4, fy = 0.4, interpolation = cv2.INTER_AREA)
cv2.imwrite('resize.jpg', resize)

cv2.waitKey(0)
cv2.destroyAllWindows()