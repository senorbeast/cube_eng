import numpy as np
import cv2 as cv
from read import rescaleFrame


img = cv.imread("Images/Rubiks_1.jpeg")
img = rescaleFrame(img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 10, 175)

# Binarize
#ret, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)

blank = np.zeros(img.shape, dtype='uint8')

# Contours
contours, hierarchies = cv.findContours(
    canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow("Cube", blank)
cv.waitKey(0)
