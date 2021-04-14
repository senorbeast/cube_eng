import numpy as np
import cv2 as cv
from color_spaces import rescaleFrame

img = cv.imread("Images/Rubiks_1.jpeg")
img = rescaleFrame(img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("thresh", thresh)

# Inversing the simple thresholding
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("thresh_inv", thresh_inv)

# Adaptive Thresholding (somewhat like getting edges)
adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 9)


cv.imshow("Adaptive Thresholding", adaptive_thresh)
cv.waitKey(0)
