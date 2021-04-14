import numpy as np
import cv2 as cv

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)


bitAND = cv.bitwise_and(rectangle, circle)
bitXOR = cv.bitwise_xor(rectangle, circle)
bitN = cv.bitwise_not(rectangle)
# OR available.

cv.imshow("bitAND", bitAND)
cv.imshow("bittOR", bitN)
cv.waitKey(0)
