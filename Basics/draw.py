import cv2 as cv
import numpy as np
img = cv.imread("./Images/Rubiks_1.jpeg")

# blank = np.zeros((500, 500, 3), dtype="uint8")

# blank[200:300, 300:400] = 0, 0, 255

# cv.rectangle(blank, (0, 0),
#              (blank.shape[1]//2, blank.shape[1]//2), (0, 255, 0), thickness=2)


# cv.circle(blank,
#           (blank.shape[1]//2, blank.shape[1]//2), 40, (0, 255, 0), thickness=2)


# cv.line(blank, (100, 250),
#         (300, 400), (0, 255, 0), thickness=2)

# cv.putText(blank, "Hello", (255, 255), cv.FONT_HERSHEY_TRIPLEX,
#            1.0, (255, 255, 0), thickness=2)
cv.imshow("Drawing", img)
cv.waitKey(0)
