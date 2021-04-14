import cv2 as cv
import read

img = cv.imread("Images/Rubiks_1.jpeg")
img = read.rescaleFrame(img, 0.5)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Blur
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)

# Edge Cascade
canny = cv.Canny(img, 100, 175)
resizedC = read.rescaleFrame(canny, 0.7)
#cv.imshow("Canny", resizedC)

# Dilating the IMage
dilated = cv.dilate(canny, (3, 3), iterations=3)

# Eroded the IMage
eroded = cv.erode(dilated, (3, 3), iterations=3)
reCR = read.rescaleFrame(eroded, 0.7)
#cv.imshow("Eroded", reCR)

# Cropped Image
#cropped = img[50:200, 200:400]

# Showing image
cv.imshow("Original", img)
cv.waitKey(0)
