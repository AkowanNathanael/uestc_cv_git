import cv2 as cv
cap = cv.VideoCapture("vid.mp4")
while True:
    success, frame = cap.read()
    if not success:
        break
    cv.imshow("win frame", frame)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
cv.destroyAllWindows()
