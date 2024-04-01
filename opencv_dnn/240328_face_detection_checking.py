import pickle
import time

import cv2
import face_recognition

image_file = './image/marathon_01.jpg'
encoding_file = 'encodings.pickle'
unknown_name = 'Unknown'
model_method = 'cnn'

def detectAndDisplay(image):
    start_time = time.time()
    rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(rgb,
                                            model = model_method)
    encodings = face_recognition.face_encodings(rgb, boxes)

    names = []

    for encoding in encodings:

        #데이터 확인 값을 매칭
        matches = face_recognition.compare_faces(data["encodings"],
                                                 encoding)
        name = unknown_name

        #목표를 찾아쓴ㄴ지 확이
        if True in matches:

            matchedIdxs = [i for (i,b) in enumerate(matches) if b]
            counts = {}

            #어떤 이름으로 매칭이 되었는지 확인인
            for i in matchedIdxs:
                name = data["name"][i]
                counts[name] = counts.get(name,0) + 1

            # 가장 많이 나온 이름으로 판단단
            name = max(counts, key=counts.get)

        names.append(name)

    #이제 확인이 끝났으니 확인된 내용을 바탕으로 표시하기
    for ((top,right,bottom, left),name) in zip(boxes,names):
        y = top - 15 if top -15 > 15 else top +15
        color = (0,255,0)
        line = 2
        if (name == unknown_name):
            color = (0,0,255)
            line = 1
            name = ''
        cv2.rectangle(image, (left,top),(right,bottom), color, line)
        y = top - 15 if top - 15 > 15 else top + 15
        cv2.putText(image, name, (left,y), cv2.FONT_HERSHEY_PLAIN, 1, color, line)

    end_time = time.time()
    process_time = end_time - start_time
    print(f'process time : {process_time}')
    cv2.imshow("Recognition",image)

data= pickle.load(open(encoding_file,"rb"))

image = cv2.imread(image_file)
detectAndDisplay(image)

cv2.waitKey(0)
cv2.destroyAllWindows()