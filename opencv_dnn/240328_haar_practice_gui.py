import cv2
import numpy as np
#GUI 용 패키지
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog

# definition
face_cascade_name = './data/haarcascades/haarcascade_frontalface_alt.xml'
eyes_cascade_name = './data/haarcascades/haarcascade_eye_tree_eyeglasses.xml'
file_name = "./image/marathon_02.jpg"
title_name = 'Haar cascade object detection'
# 사이즈가 커지면 인식률이 높아지기도 해
frame_width = 500



def selectFile():
    file_name =  filedialog.askopenfilename(initialdir = "./image",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print('File name : ', file_name)
    read_image = cv2.imread(file_name)
    (height, width) = read_image.shape[:2]
    frameSize = int(sizeSpin.get())
    ratio = frameSize / width
    dimension = (frameSize, int(height * ratio))
    read_image = cv2.resize(read_image, dimension, interpolation = cv2.INTER_AREA)
    image = cv2.cvtColor(read_image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    imgtk = ImageTk.PhotoImage(image=image)
    detectAndDisplay(read_image)

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
    # cv2.imshow('Capture - Face detection', frame)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    imgtk = ImageTk.PhotoImage(image=image)
    detection.config(image=imgtk)
    detection.image = imgtk

#main (tkinter)
main = Tk()
main.title(title_name)
main.geometry()


read_img = cv2.imread("./image/marathon_02.jpg")

print(f'width : {read_img.shape[1]} pixels')
print(f'height : {read_img.shape[0]} pixels')
print(f'channels : {read_img.shape[2]} pixels')
# Image Resize
(height, width) = read_img.shape[:2]
ratio = frame_width / width
dimension = (frame_width, int(height * ratio))
read_image = cv2.resize(read_img,dimension, interpolation=cv2.INTER_AREA)

#tkinter에 대해서 gui로 보여주기
image = cv2.cvtColor(read_image,cv2.COLOR_BGR2RGB)
image = Image.fromarray(image)
imgtk = ImageTk.PhotoImage(image=image)

# cv2.imshow("Original Image",img)



face_cascade = cv2.CascadeClassifier()
eyes_cascade = cv2.CascadeClassifier()

if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)
if not eyes_cascade.load(cv2.samples.findFile(eyes_cascade_name)):
    print('--(!)Error loading eyes cascade')
    exit(0)

# detectAndDisplay(img)
# 아래부터 tk로 실행
label=Label(main, text=title_name)
label.config(font=("Courier", 18))
label.grid(row=0,column=0,columnspan=4) # 그리드형식
sizeLabel=Label(main, text='Frame Width : ')
sizeLabel.grid(row=1,column=0)
sizeVal  = IntVar(value=frame_width)
sizeSpin = Spinbox(main, textvariable=sizeVal,from_=0, to=2000, increment=100, justify=RIGHT)
sizeSpin.grid(row=1, column=1)
Button(main,text="File Select", height=2,command=lambda:selectFile()).grid(row=1, column=2, columnspan=2, sticky=(W, E))
detection=Label(main, image=imgtk)
detection.grid(row=2,column=0,columnspan=4)
detectAndDisplay(read_image)


cv2.waitKey(0)
cv2.destroyAllWindows()