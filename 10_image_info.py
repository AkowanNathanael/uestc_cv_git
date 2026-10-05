import cv2 as cv
img = cv.imread("dev.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # type:ignore
print(gray.shape)
print(gray.size)
print(gray.dtype)
print(gray.ndim)
print(img.shape)
print(img.size)
print(img.dtype)
print(img.ndim)
cv.destroyAllWindows()
