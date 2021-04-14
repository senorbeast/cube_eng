import numpy as np
import cv2 as cv
from color_spaces import rescaleFrame

img = cv.imread("Images/Rubiks_1.jpeg")
img = rescaleFrame(img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)
cv.imshow("Original", img)
# cv.imshow("b", b)
# cv.imshow("g", g)
# cv.imshow("r", r)

# print(img.shape)
# print(b.shape)
# print(g.shape)
# print(r.shape)

bgr = cv.merge([b, g, r])
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
cv.imshow('merged', bgr)
cv.imshow("blue", blue)
cv.imshow("green", green)
cv.imshow("red", red)

cv.waitKey(0)
