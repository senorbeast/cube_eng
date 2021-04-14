import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Images/Rubiks_1.jpeg")


def rescaleFrame(frame, scale=0.5):
    # Works for images, videos, live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = rescaleFrame(img, 0.5)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
kernel = np.ones((2, 2), np.uint8)

# HSV -> GAUSSIANBlur -> CANNY
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
blur = cv.GaussianBlur(hsv, (15, 15), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 10, 175)


blank = np.zeros(img.shape, dtype='uint8')
# Contours
contours, hierarchies = cv.findContours(
    canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found')
print()
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)

dilation = cv.dilate(blank, kernel, iterations=1)

cv.imshow("Cube", hsv)
cv.waitKey(0)
