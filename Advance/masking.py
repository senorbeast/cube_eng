import numpy as np
import cv2 as cv
from color_spaces import rescaleFrame

img = cv.imread("Images/Rubiks_1.jpeg")
img = rescaleFrame(img)
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)
print(img.shape)
mask = cv.circle(
    blank, (img.shape[2]//2 + 250, img.shape[1]//2 + 50), 100, 255, -1)
cv.imshow("Mask", mask)
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("og", masked)
cv.waitKey(0)
