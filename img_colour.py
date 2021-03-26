# %%
import cv2
import numpy as np

# %%
# read image
img = cv2.imread('Rubiks_1.jpeg')

# %%
# convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# invert gray image
gray = 255 - gray

# threshold
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]

# apply close and open morphology to fill tiny black and white holes and save as mask
kernel = np.ones((3, 3), np.uint8)
mask = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# get contours (presumably just one around the nonzero pixels)
contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]
cntr = contours[0]
x, y, w, h = cv2.boundingRect(cntr)

# make background transparent by placing the mask into the alpha channel
new_img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
new_img[:, :, 3] = mask

# then crop it to bounding rectangle
crop = new_img[y:y+h, x:x+w]
# show the images
cv2.imshow("CROP", crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
