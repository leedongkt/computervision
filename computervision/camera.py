import cv2 as cv
import sys

cap=cv.VideoCapture(0,cv.CAP_DSHOW) # 카메라와 연결 시도 

if not cap.isOpened():
    sys.exit("카메라 연결 실패")

while True:
    ret,frame=cap.read()  # 비디오를 구성하는 프레임 획득

    if not ret:
        print("프레임 획득에 실패하여 루프 나가자")
        break

    cv.imshow('video display', frame)

    key=cv.waitKey(1)   #1 밀리초 동안 키보드 입력 기다림
    if key==ord('q'): # q 키 들어오면 루프 브레이크
        break

cap.release()  # 카메라와 연결 끊음 
cv.destroyAllWindows()

