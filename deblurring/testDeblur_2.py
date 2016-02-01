from __future__ import print_function
import numpy as np
import cv2
import pytesseract

# URL:http://en.wikipedia.org/wiki/Wiener_deconvolution
def blur_edge(img, d=31):
    h, w  = img.shape[:2]
    img_pad = cv2.copyMakeBorder(img, d, d, d, d, cv2.BORDER_WRAP)
    img_blur = cv2.GaussianBlur(img_pad, (2*d+1, 2*d+1), -1)[d:-d,d:-d]
    y, x = np.indices((h, w))
    dist = np.dstack([x, w-x-1, y, h-y-1]).min(-1)
    w = np.minimum(np.float32(dist)/d, 1.0)
    return img*w + img_blur*(1-w)

def motion_kernel(angle, d, sz=65):
    kern = np.ones((1, d), np.float32)
    c, s = np.cos(angle), np.sin(angle)
    A = np.float32([[c, -s, 0], [s, c, 0]])
    sz2 = sz // 2
    A[:,2] = (sz2, sz2) - np.dot(A[:,:2], ((d-1)*0.5, 0))
    kern = cv2.warpAffine(kern, A, (sz, sz), flags=cv2.INTER_CUBIC)
    return kern

def defocus_kernel(d, sz=65):
    kern = np.zeros((sz, sz), np.uint8)
    cv2.circle(kern, (sz, sz), d, 255, -1, cv2.LINE_AA, shift=1)
    kern = np.float32(kern) / 255.0
    return kern

'''
Input
For this 2.png, d which is blured pixel length =27.3 is the best.
'''
fn = '../deblurring/2.png'
ang=0
d=27.3
noise=0.0001

#Calculation
ang=np.deg2rad(ang)
img = cv2.imread(fn, 0)
img = np.float32(img)/255.0
cv2.imshow('input', img)
IMG = cv2.dft(img, flags=cv2.DFT_COMPLEX_OUTPUT)
psf = motion_kernel(ang, d)
#cv2.imshow('psf', psf)
psf /= psf.sum()
psf_pad = np.zeros_like(img)
kh, kw = psf.shape
psf_pad[:kh, :kw] = psf
PSF = cv2.dft(psf_pad, flags=cv2.DFT_COMPLEX_OUTPUT, nonzeroRows = kh)
PSF2 = (PSF**2).sum(-1)
iPSF = PSF / (PSF2 + noise)[...,np.newaxis]
RES = cv2.mulSpectrums(IMG, iPSF, 0)
res = cv2.idft(RES, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT )
res = np.roll(res, -kh//2, 0)
res = np.roll(res, -kw//2, 1)

#Result
cv2.imshow('Output',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
