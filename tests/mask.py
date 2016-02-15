import numpy as np
import cv2
from PIL import Image
import pytesseract
import sys
from matplotlib import pyplot as plt
import getopt

def make_mask(filename):
    
    #opts, args = getopt.getopt(sys.argv[1:], '')
    #filename = args[0]

    
    #### read image
    src = cv2.imread(filename, cv2.IMREAD_COLOR)
    #blur = np.ones((src.shape[0],src.shape[1]), np.uint8)
    #cv2.medianBlur(src, 3, src)
    #cv2.imshow('blurred', src)
    
    dst = cv2.cvtColor(src, cv2.COLOR_BGR2HSV) 
    
    ##Thresholding!
    mask=np.zeros((src.shape[0],src.shape[1]), np.uint8)
    red_mat=src[:,:,2]
    blue_mat=src[:,:,0]
    green_mat=src[:,:,1]
    idx1=np.greater(green_mat,red_mat*2)
    idx2=np.greater(blue_mat,red_mat*2)
    result_rgb=np.logical_and(idx1,idx2)
    
    hue_mat=dst[:,:,0]
    sat_mat=dst[:,:,1]
    val_mat=dst[:,:,2]
    idx1=np.greater(hue_mat,0.4*180)
    idx2=np.less(hue_mat,0.56*180)
    idx3=np.greater(sat_mat,0.4*255)
    result_hsv=np.logical_and(idx1,idx2)
    result_hsv=np.logical_and(result_hsv,idx3)
    
    result_bt=np.less(red_mat,8)
    
    result=np.logical_and(result_hsv,result_rgb)
    result=np.logical_or(result,result_bt)
    mask[result]=255;
    cv2.imshow('Mask Output',mask)

    cv2.imwrite('mask.png', mask)
    message = pytesseract.image_to_string(Image.open('mask.png'))
    print "=====Mask tesseract output======"
    print message
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 
    
