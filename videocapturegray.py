import cv2 as cv
  
capture = cv.VideoCapture(0)
  
while(True):
      
    ret, frame = capture.read()
 
    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
 
    cv.imshow('video gray', grayFrame)
   
      
    if cv.waitKey(1) == 27:
        break