import cv2
import numpy as np 
import sys
import pytesseract
import math
from PIL import Image
from matplotlib import pyplot as plt


file_ori = '/Users/xuez/Documents/RHIT/YGR1/test/DSC_0645.JPG';
file_comp = '/Users/xuez/Desktop/test/DSC_0645.JPG'

ori = cv2.imread(file_ori)
comp = cv2.imread(file_comp)
gray_ori = cv2.cvtColor(ori, cv2.COLOR_RGB2GRAY)
grap_comp = cv2.cvtColor(comp, cv2.COLOR_RGB2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17,17 )
cv2.imshow('gray',gray)

'''
	#Mask
    
    make_mask('preproced.png')

    #Rotate

    rotate('mask.png')
 '''