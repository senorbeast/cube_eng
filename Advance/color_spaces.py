import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


def rescaleFrame(frame, scale=0.5):
    # Works for images, videos, live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# img = cv.imread("Images/Rubiks_1.jpeg")
# img = rescaleFrame(img)

# # BGR to Grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# # BGR to HSV
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# # BGR to L*a*b
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# canny = cv.Canny(lab, 150, 255)


# # BGR to RGB
# rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# # HSV to BGR and all

# cv.imshow("Original", img)

# # cv.imshow("hsv", hsv)

# # cv.imshow("lab", lab)

# cv.imshow("rgb", rgb)
# plt.imshow(rgb)
# plt.show()
# cv.waitKey(0)
