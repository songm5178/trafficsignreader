import numpy as np
import cv2
from PIL import Image
import pytesseract

# Load an color image in grayscale
img = cv2.imread('alphabets.jpg',0)

message = pytesseract.image_to_string(Image.open('alphabets.jpg'))
print message
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()