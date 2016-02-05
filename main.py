import numpy as np
import cv2
from PIL import Image
import pytesseract
import sys
from matplotlib import pyplot as plt

if __name__ == '__main__':
    # read image
    src = cv2.imread('traff1.jpg', cv2.IMREAD_COLOR)
    dst = cv2.cvtColor(src, cv2.COLOR_RGB2HSV)  
    ##### Use this to find coordinates ####
    # plt.imshow(dst, cmap = 'gray', interpolation = 'bicubic')
    # plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    # plt.show()    

    # extract green color from HSV

    
    # ij_index = [-1, -1] 
    # max_h = -1
    # for i in range (dst.shape[0]):
        # for j in range (dst.shape[1]):

            # if (dst[i,j][0] >= 35 and dst[i,j][0] < 40 and \
                # dst[i,j][1] >= 40 and dst[i,j][2] < 50 and dst[i,j][2] > 240):
                # cv2.circle(dst,(j, i),5,(255, 0, 255))

            # else:
                # cv2.circle(dst,(j, i),5,(0,0,0))
    print dst[200, 490]
    print dst[200, 430]
    print dst[200, 200]
    print dst[200, 100]
    lower_green = np.array([40, 220, 120])
    upper_green = np.array([50, 255, 160])
    green_mask = cv2.inRange(dst, lower_green, upper_green)
    res = cv2.bitwise_and(src, src, mask= green_mask)
  
    
    cv2.imshow('src',src)
    cv2.imshow('mask', green_mask)
    cv2.imshow('res', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
    # extract traffic sign shape
    
    
    # run tesseract on traffic sign

    