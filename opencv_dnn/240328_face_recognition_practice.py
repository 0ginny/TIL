import cv2
import face_recognition
import pickle

dataset_paths =  ['./dataset/son/','./dataset/tedy/']
names = ['Son', 'Tedy']
number_images = 10
image_type = '.jpg'
encoding_file = 'encodings.pickle'

#보통 cnn 이나 hog를 써
#cnn은 느리지만 정확하고 hog는 빠르지만 정확도가 조금 낮아
model_method = 'cnn'

knownEncodings = []
knownNames =[]

for (i, dataset_path) in enumerate(dataset_paths) :
    # 각각 폴더 이름별로 반복 (Son, Tedy ...)
    name = names[i]

    for idx in range(number_images):
        # 파일명을 1~ 10.jpg로 했지
        file_name = dataset_path + str(idx+1) + image_type
        #image load and change rgb
        image = cv2.imread(file_name)
        rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        # face recognition 라이브러리를 통해 얼굴 박스
        boxes = face_recognition.face_locations( rgb,
                                                 model = model_method)
        # conpute the facial embedding for the face
        encodings = face_recognition.face_encodings(rgb, boxes)

        #loop over the encodings
        for encoding in encodings :
            print(file_name, name,encoding)
            knownEncodings.append(encoding)
            knownNames.append(name)

# 학습 모델 저장
data = {"encodings" : knownEncodings, "name": knownNames}
f = open(encoding_file, "wb")
f.write(pickle.dumps(data))