import cv2 as cv
img = cv.imread('css-shapes.jpg' ,1)
resized_image = cv.resize(img, (800, 600))
cv.imshow('Resize', resized_image)
cv.waitKey(0)
cv.destroyAllWindows()