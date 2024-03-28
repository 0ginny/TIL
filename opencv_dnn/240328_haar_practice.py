import cv2
import numpy as np

"""
감지 함수
"""
def detectAndDisplay(frame):
    #채널이 많아지면 오류가 생길 수 있으므로 그레이 필터 적용
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)
    #-- 감지
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        center = (x + w //2, y + h//2) #감지된 중앙 좌표
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 4) #감지후 네모로 표시
        faceROI = frame_gray[y:y+h, x:x+w] #찾아낸 얼굴만 가져와서 눈 찾으려고
        # IN each face, detect eyes
        # 눈 표시
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2 //2, y + y2 + h2//2) #감지된 눈 중앙 좌표
            radius = int(round((w2+h2)/4))
            frame = cv2.circle(frame,eye_center,radius, (255,0,0),4)
    cv2.imshow('Capture - Face detection', frame)


img = cv2.imread("./image/marathon_02.jpg")

print(f'width : {img.shape[1]} pixels')
print(f'height : {img.shape[0]} pixels')
print(f'channels : {img.shape[2]} pixels')

(height, width) = img.shape[:2]

cv2.imshow("Original Image",img)

face_cascade_name = './data/haarcascades/haarcascade_frontalface_alt.xml'
eyes_cascade_name = './data/haarcascades/haarcascade_eye_tree_eyeglasses.xml'


face_cascade = cv2.CascadeClassifier()
eyes_cascade = cv2.CascadeClassifier()

if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)
if not eyes_cascade.load(cv2.samples.findFile(eyes_cascade_name)):
    print('--(!)Error loading eyes cascade')
    exit(0)

detectAndDisplay(img)

cv2.waitKey(0)
cv2.destroyAllWindows()