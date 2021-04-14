import numpy as np
import cv2 as cv
from color_spaces import rescaleFrame

img = cv.imread("Images/Rubiks_1.jpeg")
img = rescaleFrame(img)

# Averaging
#   just averaging values in kernel with weithgs 1
average = cv.blur(img, (7, 7))

# Gaussian Blur (different weights values in kernel)
gauss = cv.GaussianBlur(img, (7, 7), 0)

# Median Blur (a bit painting like)
median = cv.medianBlur(img, 7)

# Bilateral bluring (retaining edges.. op)
bilateral = cv.bilateralFilter(img, 10, 15, 15)

cv.imshow("Median Blur", bilateral)
cv.imshow("og", img)

cv.waitKey(0)
