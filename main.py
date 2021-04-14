# %%
import cv2
import numpy as np
from matplotlib import pyplot as plt

# %%
img = cv2.imread("Images/Rubiks_1.jpeg")


def rescaleFrame(frame, scale=0.5):
    # Works for images, videos, live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)


img = rescaleFrame(img, 0.5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# #%%
# WEBCAM FEED
# cap = cv.VideoCapture(0)

# # Check if the webcam is opened correctly
# if not cap.isOpened():
#     raise IOError("Cannot open webcam")

# while True:
#     ret, frame = cap.read()
#     frame = cv.resize(frame, None, fx=0.5, fy=0.5,
#                        interpolation=cv2.INTER_AREA)
#     cv2.imshow('Input', frame)

#     c = cv.waitKey(1)
#     if c == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()
# %%

# K- MEANS CLUSTERING TO GET THE COLORS

# Z = img.reshape((-1, 3))
# print(np.shape(Z))
# # convert to np.float32
# Z = np.float32(Z)

# # define criteria, number of clusters(K) and apply kmeans()
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# K = 10
# ret, label, center = cv2.kmeans(
#     Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# # Now convert back into uint8, and make original image
# center = np.uint8(center)
# res = center[label.flatten()]
# res2 = res.reshape((img.shape))

# %%

# hsv = cv2.cvtColor(res2, cv2.COLOR_BGR2HSV)
# cv2.imshow("HSV", hsv)

# %%
# SHI-TOMASI CORNER DETECTOR
# corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
# corners = np.int0(corners)

# for i in corners:
#     x, y = i.ravel()
#     cv2.circle(img, (x, y), 3, 255, -1)

# plt.imshow(img)
# plt.show()

# %%
# find Harris corners
# gray = np.float32(gray)
# dst = cv2.cornerHarris(gray, 2, 3, 0.04)
# dst = cv2.dilate(dst, None)
# ret, dst = cv2.threshold(dst, 0.01*dst.max(), 255, 0)
# dst = np.uint8(dst)

# # find centroids
# ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

# # define the criteria to stop and refine the corners
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
# corners = cv2.cornerSubPix(gray, np.float32(
#     centroids), (5, 5), (-1, -1), criteria)

# # Now draw them
# res = np.hstack((centroids, corners))
# res = np.int0(res)
# img[res[:, 1], res[:, 0]] = [0, 0, 255]
# img[res[:, 3], res[:, 2]] = [0, 255, 0]
# gray = np.float32(gray)
# dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# # result is dilated for marking the corners, not important
# dst = cv2.dilate(dst, None)

# # Threshold for an optimal value, it may vary depending on the image.
# img[dst > 0.01*dst.max()] = [0, 0, 255]
# # cv2.imwrite('subpixel5.png', img)
# %%

im = cv2.bilateralFilter(img, 9, 75, 75)
im = cv2.fastNlMeansDenoisingColored(im, None, 10, 10, 7, 21)
hsv_img = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)   # HSV image


# HSV color code lower and upper bounds
COLOR_MIN = np.array([20, 100, 100], np.uint8)
COLOR_MAX = np.array([30, 255, 255], np.uint8)       # color yellow

frame_threshed = cv2.inRange(
    hsv_img, COLOR_MIN, COLOR_MAX)     # Thresholding image
imgray = frame_threshed
ret, thresh = cv2.threshold(frame_threshed, 127, 255, 0)
contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# print type(contours)
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    print(x, y)
    cv2.rectangle(im, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow("Show", im)
cv2.imwrite("extracted.jpg", im)


# %%

# Showing image
cv2.imshow("Original", img)
cv2.waitKey(0)

# %%
