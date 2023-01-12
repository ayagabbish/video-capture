import cv2 as cv

cap = cv.VideoCapture(0)

success, frame = cap.read()
while success:
    success, frame = cap.read()
    canny = cv.cvtColor(frame, cv.COLOR_BGRA2GRAY)
    canny = cv.GaussianBlur(canny, ksize=(7, 7), sigmaX=5)
    canny = cv.Canny(canny, 50, 50)
    cv.circle(canny, (20, 20), 20, (100, 0, 10), )
    cv.imshow('Circle Image', canny)
    cv.circle(canny, (620, 20), 20, (100, 0, 10), )
    cv.imshow('Circle Image', canny)
    cv.circle(canny, (20, 455), 20, (100, 0, 10), )
    cv.imshow('Circle Image', canny)
    cv.circle(canny, (620, 450), 20, (100, 0, 10), )
    cv.imshow('Circle Image', canny)
    cv.putText(canny, "edge detection", (20, 20), cv.FONT_HERSHEY_DUPLEX, 5, (0, 0, 255))
    cv.imshow( 'canny', canny)

    #cv.imshow("Original", frame)
    cv.imshow("Canny", canny)
    key = cv.waitKey(1)
    if key == ord('q') or key == ord('Q'):
        break