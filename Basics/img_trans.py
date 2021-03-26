import numpy as np
import cv2 as cv
from read import rescaleFrame


# Translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])  # tuple of width, height
    return cv.warpAffine(img, transMat, dimensions)

# Rotation


def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    print(img.shape)
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)


img = cv.imread("Images/Rubiks_1.jpeg")

rotated = rotate(img, 45)
translated = translate(img, 50, 50)
resized = rescaleFrame(rotated)
cv.imshow("Cube", resized)
cv.waitKey(0)
