import numpy as np
import cv2
from PIL import Image
import pytesseract
import sys
from matplotlib import pyplot as plt
from mask import make_mask
from rotate import rotate

if __name__ == '__main__':
    
    filename = 'DSC_0634.jpg'
    src = cv2.imread(filename, cv2.IMREAD_COLOR)
    
    #Pre-processing
    """
    blur = np.ones((src.shape[0],src.shape[1]), np.uint8)
    cv2.medianBlur(src, 3, src)
    """
    cv2.imshow('preproced', src)
    cv2.imwrite('preproced.png', src)
    
    #Mask
    
    make_mask('preproced.png')

    #Rotate

    rotate('mask.png')

    #tesseract Output
    print "=====After Rotation Tesseract output======"
    message = pytesseract.image_to_string(Image.open('rotated.png'))
    print message
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
    
