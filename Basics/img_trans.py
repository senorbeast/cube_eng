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
img = rescaleFrame(img)
# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)

# Flipping (Upside-Down and Mirror Images)
flip = cv.flip(img, 0)

# Crop (Somewhat like list slicing but here coordinates are needed)
cropped = img[200:400, 300:400]

rotated = rotate(img, 45)
rot_rot = rotate(rotated, 45)
translated = translate(img, 50, 50)

cv.imshow("Cube", rot_rot)
cv.waitKey(0)
