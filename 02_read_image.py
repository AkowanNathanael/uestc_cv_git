# Reading image using opencv-python
import cv2 as cv
# use read function to reead imimage
imageurl = "./dev.png"  # image location use either relative or absolute path
# read image path
image1 = cv.imread(imageurl)
# pulse the imae screen show with wait time of infinity using 0
cv.imshow("frame name", image1)#type:ignore
cv.waitKey(0)
cv.destroyAllWindows()
