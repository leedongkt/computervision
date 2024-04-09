import cv2 as cv
import sys

img=cv.imread('apples.jpg')

if img is None:
    sys.exit("파일을 찾을 수 없습니다")

print(img.shape)

cv.rectangle(img, (0,0),(200,200),(255,0,0),3) #직사각형 그리기
cv.putText(img, 'sex', (0,400), cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2) #putText(이미지 변수,넣을 문자, 문자열 왼쪽 아래 구석점 좌표, 폰트 종류, 글자 크기, 글자색, 글자 두께
#계속 B G R 형식이네 
cv.imshow('Draw', img)

cv.waitKey()
cv.destroyAllWindows()