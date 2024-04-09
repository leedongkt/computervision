import cv2 as cv
import sys

img=cv.imread('soccer.jpg')

cv.imshow("Image no korean Display", img)
print(img[0,0,0], img[0,0,1],img[0,0,2])

print(img[10,10,0],img[10,10,2],img[10,10,2])

print(img[947,1433,0])

cv.waitKey()
cv.destroyAllWindows()