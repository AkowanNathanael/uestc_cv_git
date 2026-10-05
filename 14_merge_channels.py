import cv2 as cv
img = cv.imread("dev.png")
b, g, r = cv.split(img)  # type:ignore
cv.imshow("blue", b)
cv.imshow("green", g)       
cv.imshow("red", r)
merged = cv.merge([b, g, r])  # type:ignore
cv.imshow("merged", merged)
cv.waitKey(0)
cv.destroyAllWindows()