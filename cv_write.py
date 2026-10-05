import cv2 as cv
img = cv.imread("dev.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # type:ignore
textImage = cv.putText(gray, "Kim Nathan", (500, 500),
                       cv.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255), 2)
# type:ignore
cv.imshow("image", textImage)  # type:ignore
cv.imwrite("textImage.png", textImage)  # type:ignore
cv.waitKey(0)
cv.destroyAllWindows()
