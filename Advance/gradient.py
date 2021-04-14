import numpy as np
import cv2 as cv
from color_spaces import rescaleFrame

img = cv.imread("Images/Rubiks_1.jpeg")
img = rescaleFrame(img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("gray", gray)

# Laplacian
# When there is transition from black to white and
# white to black there is slope change which is
#  detected with Laplacian and then this gradient
#  value is mapped for the opencv suitable image
#  value ( absolute since image pixel values can only be +ve)

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))

# Sobel
# Sobel computes gradients in 2 dir

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel y', sobely)

# Combined sobel images

combines_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Combine', combines_sobel)

# Canny
# Advanced algorithm, it uses sobel inside  aaayyy

canny = cv.Canny(gray, 150, 175)

cv.imshow("canny", canny)
cv.waitKey(0)
