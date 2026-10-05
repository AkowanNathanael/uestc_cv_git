import cv2 as cv
image = cv.imread("dev.png")
rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)  # type:ignore
cv.imshow("RGB", rgb)
cv.waitKey(0)
cv.destroyAllWindows()
