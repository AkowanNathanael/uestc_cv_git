import cv2 as cv
from typing import Any, List
image: Any = cv.imread("dev.png")
# Crop the image from y=100 to y=400 and x=200 to x=500
crop = image[100:400, 200:500]
cv.imshow("Crop", image)  # type:ignore
cv.imshow("Croped", crop)  # type:ignore
cv.waitKey(0)
cv.destroyAllWindows()
