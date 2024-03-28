import cv2
import numpy as np

print("OpenCV version : ")
print(cv2.__version__)

img = cv2.imread("qna_error.jpg")

print(f'width : {img.shape[1]} pixels')
print(f'height : {img.shape[0]} pixels')
print(f'channels : {img.shape[2]} pixels')

(height, width) = img.shape[:2]
center = (width // 2,height // 2)

# cv2.imshow('qna',img)

w = 400
h = 350

(b,g,r) = img[w,h]
print(f'Pixel as ({w}, {h}) - Red: {r}, Green: {g}, Blue: {b}')

# 이미지 변형
dot = img[50:100, 50:100]
# cv2.imshow("Dot", dot)

img[50:100, 50:100] = (0,0,255)

# 도형 그리기
cv2.rectangle(img, (150,0), (200,100), (0,255,0), 5) # 녹색 선굵기 5

cv2.circle(img, (275,75),25 , (0,255,255),-1) #  중심위치, 반지름, 노랑, 전체채우기

cv2.line(img, (350,100), (400,100), (255,0,0),5)

cv2.putText(img, 'creat', (450, 100) , cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255),4)


cv2.imshow('qna2',img)

# 이미지 변형하기
# move
move = np.float32([[1,0,-100],[0,1,100]])
moved = cv2.warpAffine(img,move,(width,height))
# cv2.imshow("moved downd : +, up : - and right : +, left -",moved)

#rotate
move2 = cv2.getRotationMatrix2D(center,-90,1.0) # 중심, 각도, scale
rotated = cv2.warpAffine(img,move2,(width,height))
# cv2.imshow("Rotated clockwise degrees",rotated)

# resize
ratio = 200.0 /width # 가로 목표 200px
dimension = (200,int(height *ratio))

resized = cv2.resize(img, dimension, interpolation = cv2.INTER_AREA)
# cv2.imshow("Resized",resized)

# flip 반전
flipped = cv2.flip(img,-1)
# cv2.imshow("Flipped horizontal 1, Vertical 0, both -1", flipped)


#mask 란? 트랜지션 같은 거야. bitwise를 사용해야해.
mask = np.zeros(img.shape[:2], dtype = "uint8")

cv2.circle(mask, center , 100, (255,255,255), -1)

# cv2.imshow("mask",mask)

masked = cv2.bitwise_and(img,img,mask = mask) #교집합만 보여주고 싶은거지, 하얀색이 1
# cv2.imshow("masked",masked)


# 채널(rgb)을 변경하기

#rgb 분해
(Blue, Green, Red) = cv2.split(img)
# cv2.imshow("Red",Red)
# cv2.imshow("Green",Green)
# cv2.imshow("blue",blue)
# cv2.waitKey(0)
#
# zeros = np.zeros(img.shape[:2], dtype = "uint8")
# cv2.imshow("Red",cv2.merge([zeros,zeros,Red]))
# cv2.imshow("Green",cv2.merge([zeros,Green,zeros]))
# cv2.imshow("blue",cv2.merge([blue,zeros,zeros]))

# filter
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray filter", gray)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("hsv filter", hsv)
lab = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
cv2.imshow("lab filter", lab)

# 채널 더하기
BGR = cv2.merge([Blue, Green,Red])
cv2.imshow("Blue, Green and Red",BGR)

cv2.waitKey(0)
# cv2.imwrite("qna_renew.png",img) # 새로 이미지 저장
cv2.destroyAllWindows()