import cv2 as cv

# img = cv.imread("Images/Rubiks_1.jpeg")
# cv.imshow("Cube", img)


def rescaleFrame(frame, scale=0.5):
    # Works for images, videos, live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# resized = rescaleFrame(img)
# cv.imshow("Cube", resized)
# cv.waitKey(0)

# # Reading Videos Webcam
# capture = cv.VideoCapture(0)
# # Reading Video
# capture = cv.VideoCapture('Video.mp4')

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow("Video", frame)

#     if cv.waitkey(20) & 0xFF == ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()


# def changeRes(width, height):
#     # Works only for live videos
#     capture.set(3, width)
#     capture.set(4, height)
