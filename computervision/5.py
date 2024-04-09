import cv2 as cv
import sys

img=cv.imread('apples.jpg')

if img is None:
    sys.exit("파일이 존재하지 않습니다")

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)    #BGR 컬러 이미지를 명암 이미지로 변환 
gray_small=cv.resize(gray,dsize=(0,0), fx=0.5, fy=0.5) #명암 이미지로 변환한 것을 반으로 축소하기 

cv.imwrite('soccer_gray.jpg', gray)
cv.imwrite('soccer_gray_small.jpg', gray_small)



cv.imshow('Color image', img)
cv.imshow('Gray image',gray)
cv.imshow('Gray image small', gray_small)

print(gray_small.shape)
print(gray.shape)

cv.waitKey()
cv.destroyAllWindows()

print(gray_small.shape)