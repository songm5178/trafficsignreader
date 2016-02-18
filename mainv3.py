import numpy as np
import cv2
from PIL import Image
import pytesseract
import sys
from matplotlib import pyplot as plt
from os import listdir
from os.path import isfile, join
from maskV3 import make_mask
from rotate import rotate


if __name__ == '__main__':

    ofile = open('results.txt', 'w')
    
    mypath = 'trafficSign/'
    nFiles = [f for f in listdir(mypath) if isfile(join(mypath,f))]
    src = np.empty(len(nFiles), dtype=object)
    for i in range(0, len(nFiles)):
        src[i] = cv2.imread(join(mypath,nFiles[i]))
        s = "=======================\nfileName: " + nFiles[i] + "\n"
        ofile.write(s)
        """
        filename = 'tests/DSC_0612.JPG'
        src = cv2.imread(filename, cv2.IMREAD_COLOR)
        """
        
        #Pre-processing
        """
        blur = np.ones((src.shape[0],src.shape[1]), np.uint8)
        cv2.medianBlur(src, 3, src)
        """
        #cv2.imshow('preproced', src[i])
        cv2.imwrite('preproced.png', src[i])
        
        #Mask
        
        make_mask('preproced.png')

        #Rotate
        
        """
        rotate('mask.png')
        """
        
        #tesseract Output
        #print "=====After Rotation Tesseract output======"
        message = pytesseract.image_to_string(Image.open('mask.png'))
        ofile.write(message)
        ofile.write("\n\n")
        #print message
        
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
    
