import cv2 as cv
# image
img = cv.imread("dev.png")
# print(img)
cv.putText(img, "Kim Nathan", (500, 500), cv.FONT_HERSHEY_DUPLEX,
           2, (0, 0, 255), 2)  # type:ignore
cv.imshow("image",img)  #type:ignore
cv.waitKey(0)
cv.destroyAllWindows()
