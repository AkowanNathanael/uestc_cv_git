import cv2 as cv
image = cv.imread("dev.png")
gryimage = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # type:ignore
cv.imshow("image", image)  # type:ignore
cv.imshow("greya", gryimage)
cv.waitKey(0)
cv.destroyAllWindows()
