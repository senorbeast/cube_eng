import numpy as np
import cv2 as cv
from color_spaces import rescaleFrame
import matplotlib.pyplot as plt

img = cv.imread("Images/Rubiks_1.jpeg")
img = rescaleFrame(img)

plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel('# of pixels')
# Color Histogram
colors = ('b', "g", "r")
blank = np.zeros(img.shape[:2], dtype='uint8')

circle = cv.circle(blank, (img.shape[1]//2, img.shape[2]//2), 100, 255, -1)

mask = cv.bitwise_and(img, img, mask=circle)
cv.imshow("Maskkk", mask)
# Histogram

for i, col in enumerate(colors):
    histr = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])

plt.show()
cv.waitKey(0)
