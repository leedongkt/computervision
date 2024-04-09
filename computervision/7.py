import cv2 as cv
import sys

img=cv.imread('soccer_gray_small.jpg')

if img is None:
    sys.exit("파일을 찾을 수 없습니다")

def draw(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:
        cv.rectangle(img,(x,y),(x+50,y+50),(0,0,255),2)
    elif event==cv.EVENT_FLAG_RBUTTON:
        cv.rectangle(img,(x,y), (x+100,y+100),(255,0,0),2)  #내가 찍은 곳 x위치가 왼쪽 상단, y위치는 오른쪽 하단으로 해서 거기서 100씩 크게해서 나타나게 

    cv.imshow('Drawing', img)


cv.namedWindow('Drawing')
cv.imshow('Drawing', img)

cv.setMouseCallback('Drawing', draw)

while(True):
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()
        break