import cv2
import numpy as np 
import sys
import pytesseract
import math
from PIL import Image
from matplotlib import pyplot as plt


def crop_img(filename):

    img = cv2.imread(filename);
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17,17 )


    edges = cv2.Canny(gray, 150, 170);
    cv2.imshow('edge', edges);

    ### contours finder

    (_, cnts, _) = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
    screenCnt = None

    for c in cnts:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        
        if len(approx) == 4:
        #if len(approx) < 9:
            screenCnt = approx
            break
            
    #print [screenCnt]


    smallest = 99999
    smallestIndex = 0
    smaller = 99999
    smallerIndex = 0

    for i in range(0, 4):
        if screenCnt[i][0][0] < smallest:
            smaller = smallest
            smallerIndex = smallestIndex
            smallest = screenCnt[i][0][0]
            smallestIndex = i
        elif screenCnt[i][0][0] > smallest and screenCnt[i][0][0] < smaller:
            smaller = screenCnt[i][0][0]
            smallerIndex = i
    left = []
    left.append(smallestIndex)
    left.append(smallerIndex)

    smallest = 99999
    smallestIndex = 0
    smaller = 99999
    smallerIndex = 0
    for i in range(0, 4):
        if screenCnt[i][0][1] < smallest:
            smaller = smallest
            smallerIndex = smallestIndex
            smallest = screenCnt[i][0][1]
            smallestIndex = i
        elif screenCnt[i][0][1] > smallest and screenCnt[i][0][1] < smaller:
            smaller = screenCnt[i][0][1]
            smallerIndex = i
    top = []
    top.append(smallestIndex)
    top.append(smallerIndex)

    leftTop = 0
    leftBottom = 0
    rightTop = 0
    rightBottom = 0
    for i in range(0, 4):
        if i in left:
            if i in top:
                leftTop = i
            else:
                leftBottom = i
        else:
            if i in top:
                rightTop = i
            else:
                rightBottom = i
    
    dx = screenCnt[rightTop][0][0] - screenCnt[leftTop][0][0]
    dy = screenCnt[rightTop][0][1] - screenCnt[leftTop][0][1]
    angle = math.degrees(math.atan2(-dy, dx))
    centerx = 0
    centery = 0
    for i in range(0, 4):
        centerx = centerx + screenCnt[i][0][0]
        centery = centery + screenCnt[i][0][1]
    centerx = centerx / 4
    centery = centery / 4
    (rows, cols, _) = img.shape

    M = cv2.getRotationMatrix2D((centerx,centery),-angle, 1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    cv2.imshow("asdf", dst)

    #screenCnt = cv2.convexHull(screenCnt)
    cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)
    cv2.imshow("traffic", img)

    crop_img = img[screenCnt[leftTop][0][1]-50:screenCnt[leftBottom][0][1]+50, screenCnt[leftTop][0][0]-50:screenCnt[rightBottom][0][0]+50]
    cv2.imshow('crop_img', crop_img)

    cv2.imwrite('cropped.png', crop_img)

    ### hough detection
    '''
    minLineLength = 100
    maxLineGap = 10
    lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
    for x1,y1,x2,y2 in lines[0]:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

    cv2.imshow('hough img', img)
    '''


    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return
