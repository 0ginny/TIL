import time

import cv2
import numpy as np

file_name = './video/yolo_01.mp4'
min_confidence = 0.5

def detectAndDisplay(frame):
    start_time = time.time() # 프레임당 시간 측정

    img = cv2.resize(frame, None, fx=0.6, fy =0.6)
    height, width, channels = img.shape
    cv2.imshow("Original image", img)

    # detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)
    outs = net.forward(output_layers)

    # showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > min_confidence:
                # object tdetected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # noise 없애기, not maxi??
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, min_confidence, 0, 4)
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            # 화면에 어떤 거 확인되고 confidence까지
            label = f'{classes[class_ids[i]]} : {confidences[i]*100:.2f}%'
            print(i, label)
            color = colors[i]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y - 5), font, 2, color, 2) #박스위에 label 위치
    cv2.imshow("YOLO image", img)

    #frame당 시간 측정
    end_time = time.time()
    process_time = end_time - start_time
    print(f'frame seconds : {process_time:.3f} s')

########  load yolo
# yolo cite 에서 얻을 수 있음
# pjreddie.com
net = cv2.dnn.readNet("./yolo/yolov3.weights","./yolo/yolov3.cfg")
classes = []
with open("./yolo/coco.names","r") as f:
    classes = [line.strip() for line in f.readlines()]
#yolo의 작동방식
layer_names = net.getLayerNames()
print(layer_names)
print(net.getUnconnectedOutLayers())
print(layer_names[net.getUnconnectedOutLayers()[0]])
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
# 물건마다 색을 다르게 해보자
colors = np.random.uniform(0, 255, size = (len(classes),3))

#### read the video stream
cap = cv2.VideoCapture(file_name)
if not cap.isOpened :
    print("open error")
    exit(0)
while True:
    ret, frame = cap.read()
    if frame is None:
        print("No Captured frame")
        break
    detectAndDisplay(frame)
    # q를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break


cv2.waitKey(0)
cv2.destroyAllWindows()