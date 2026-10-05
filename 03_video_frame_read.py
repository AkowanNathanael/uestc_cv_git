import cv2 as cv

video_capture = cv.VideoCapture(0)
while True:
    success, frame = video_capture.read()
    if not success:
        break
    cv.imshow("win frame", frame)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cv.destroyAllWindows()
