import cv2
import numpy as np


image = cv2.imread("Images/Rubiks_1.jpeg")

# * Preprocessing - resized image to be used, making a copy, blank array for mask ✅
# * HSV Filtering - selecting different ranges of colours to filter ✔
# * Make the ranges adaptable or user Adjustable
# * Morphology - to remove noise ✅
# * Selecting the Cube Contour* - (Removed contours touching the boundaries, and contours with small areas)✅


def rescaleFrame(frame, scale=0.5):
    # Works for images, videos, live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)


image = rescaleFrame(image, 0.5)

original = image.copy()
cv2.imshow("Original Image ", image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#cv2.imshow("HSV Image ", image)

mask = np.zeros(image.shape, dtype=np.uint8)

# * HSV
# Hue - 0 to 180 (diff colors)
# Saturation - 0 to 255 (white to color)
# Value - 0 to 255 (black to white)

colors = {
    'white': ([0, 0, 200], [180, 20, 255]),  # White
    'blue': ([69, 170, 140], [150, 255, 255]),    # Blue
    'yellow': ([21, 110, 117], [45, 255, 255]),   # Yellow
    'orange': ([0, 170, 125], [17, 255, 255]),    # Orange
    'green': ([45, 35, 140], [69, 255, 255]),   # Green
    'red': ([150, 35, 140], [179, 255, 255]),        # Red
}

# Color threshold to find the squares
# * Kernel for morphological operations
open_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
close_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
for color, (lower, upper) in colors.items():
    # Coverting the arrays to be used in openCV
    lower = np.array(lower, dtype=np.uint8)
    upper = np.array(upper, dtype=np.uint8)
    # Creating a mask of the colors in range
    color_mask = cv2.inRange(image, lower, upper)

    #Opening and closgin
    # color_mask = cv2.morphologyEx(
    #     color_mask, cv2.MORPH_OPEN, open_kernel, iterations=1)
    color_mask = cv2.morphologyEx(
        color_mask, cv2.MORPH_CLOSE, close_kernel, iterations=5)

    color_mask = cv2.merge([color_mask, color_mask, color_mask])

    # Adding all color_masks to mask
    mask = cv2.bitwise_or(mask, color_mask)
    #cv2.imshow(f"Cube - {color}", color_mask)


# Shrink to 1 channel to be morphed (to be used further)
gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

# Opening and closing the combined mask
gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, close_kernel)
gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, open_kernel)

# Now finding all contours of the HSV processed image
cnts = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

# print(f"{len(cnts)} contours found in Image")

# Masking with the HSV filter
masked_out = cv2.bitwise_and(original, original, mask=gray)
#cv2.imshow("HSV Filtering", masked_out)

# * Removing contours from the boundaries of the image (remove unneccesary part)
ncnts = []
for cnt in cnts:
    x, y, w, h = cv2.boundingRect(cnt)
    if (min(x, y, w, h) == 0 or x+w == masked_out.shape[1]) == False:
        ncnts.append(cnt)


# * Now selecting the contour with the largest area (the cube)

mask_2 = np.zeros(image.shape, dtype=np.uint8)
cv2.drawContours(
    mask_2, [max(ncnts, key=cv2.contourArea)], -1, (255, 255, 255), -1)


#cv2.imshow("Final mask - after more contour filtering", mask_2)
mask_2 = cv2.cvtColor(mask_2, cv2.COLOR_BGR2GRAY)
final_op = cv2.bitwise_and(original, original, mask=mask_2)

cv2.imshow("Final Output", final_op)
cv2.imwrite("./Output/FinalOp.jpg", final_op)
cv2.waitKey(0)

#ROI = [max(ncnts, key=cv2.contourArea)]
# return final_op, ROI
