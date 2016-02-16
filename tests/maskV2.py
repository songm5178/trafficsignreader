import numpy as np
import cv2
from PIL import Image
import pytesseract
import sys
from matplotlib import pyplot as plt
import math
from numpy import size

def round2uint8(inputmat):
    min_value=np.min(inputmat);
    max_value=np.max(inputmat);
    diff=(max_value-min_value)*1.0
    outputmat=np.multiply(np.divide((inputmat-min_value),diff),255);
    return outputmat

def crop2uint8(inputmat):
    idx=inputmat>255
    inputmat[idx]=255
    return inputmat
    
    
    
    
if __name__ == '__main__':
    
    #### Initial Tesseract
    filename = 'traff2.jpg'

    
    #### read image
    src = cv2.imread(filename, cv2.IMREAD_COLOR)
    #blur = np.ones((src.shape[0],src.shape[1]), np.uint8)
    #cv2.medianBlur(src, 3, src)
    #cv2.imshow('blurred', src)
    
    dst = cv2.cvtColor(src, cv2.COLOR_BGR2HSV) 
    
    ##Thresholding!
    red_mat=src[:,:,2]
    blue_mat=src[:,:,0]
    green_mat=src[:,:,1]
    hue_mat=np.divide(dst[:,:,0],180.0)
    sat_mat=np.divide(dst[:,:,1],255.0)
    val_mat=np.divide(dst[:,:,2],255.0)
    img_mat_hsv=np.multiply(np.abs(1-hue_mat+0.485),np.square(sat_mat))
    img_mat_rgb=np.divide(crop2uint8(np.add(green_mat,blue_mat*1.0)),red_mat+0.01)
    img_mat_rgb=crop2uint8(img_mat_rgb)
    img_mat_hsv=round2uint8(img_mat_hsv)
    result=np.multiply(img_mat_hsv,img_mat_rgb)
    result=crop2uint8(result)
    result=np.uint8(result)
    
    result=255-result
    result=np.double(result)
    
    r=np.size(result,0)
    c=np.size(result,1)
    result_localAvg = cv2.blur(result,(r/3,c/3),None,None,cv2.BORDER_REPLICATE)
    shape=(r,c)
    mask=np.ones(shape)
    T=0.5
    mask[np.less_equal(result,result_localAvg*(1-T))]=0
    mask=1-mask
    mask=255*mask
    
    kernel = np.ones((4,4),np.uint8)
    mask_morph = cv2.dilate(mask, kernel, iterations = 1)
    mask_morph = cv2.erode(mask_morph, kernel, iterations = 1)
    
    cv2.imshow('mask',mask)
    cv2.imshow('morph',mask_morph)
    
    cv2.imwrite('mask.png', mask)
    cv2.imwrite('morphed_mask.png', mask_morph)

    print "=====Mask tesseract output======"
    message = pytesseract.image_to_string(Image.open('mask.png'))
    print(message)
    
    print "=====Mask tesseract output After morphed======"
    message = pytesseract.image_to_string(Image.open('morphed_mask.png'))
    print(message)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
    
