import cv2 as cv
img = cv.imread("dev.png")
rimg = cv.resize(img, None, fx=0.5, fy=0.5)  # type:ignore
r2img = cv.resize(img, (300, 200))  # type:ignore
cv.imshow("resized to 300x200", r2img)
cv.imshow("resized", rimg)
cv.waitKey(0)
cv.destroyAllWindows()
