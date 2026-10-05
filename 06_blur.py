import cv2 as cv
image = cv.imread("dev.png")
blur = cv.GaussianBlur(image, (5, 5), 12, 12)  # type:ignore
cv.imshow("image", image)  # type:ignore
cv.imshow("blur", blur)
cv.waitKey(0)
cv.destroyAllWindows()
