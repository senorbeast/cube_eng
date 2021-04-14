
import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Images/Rubiks_1.jpeg")


def rescaleFrame(frame, scale=0.5):
    # Works for images, videos, live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)


img = rescaleFrame(img, 0.5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.ones((2, 2), np.uint8)

# HSV -> GAUSSIANBlur -> CANNY
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([83, 100, 100])  # lower hsv range of blue colour
upper_red = np.array([113, 255, 255])  # upper hsv range of blue colour
lower = np.array([50, 0, 0, ])
# hailla abhi bhi comments padh rahe ho tum banoge asli coderss
upper = np.array([35, 0, 0, ])
# itna padh hi liyatho khud hi guess marlo
mask1 = cv2.inRange(hsv, lower, upper)
# arey last wala guess maro phir yai padhna
mask = cv2.inRange(hsv, lower_red, upper_red)

res = cv2.bitwise_and(img, img, mask=mask)

kernel = np.ones((5, 5), np.uint8)

mask = cv2.erode(mask, kernel, iterations=1)
mask = cv2.dilate(mask, kernel, iterations=1)
#closing = cv2.morphologyEx( mask ,cv2.MORPH_CLOSE ,kernel )
contours, hierarchy = cv2.findContours(
    mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0, 0, 255), 1)
cv2.imshow("Cube", img)
cv2.waitKey(0)
