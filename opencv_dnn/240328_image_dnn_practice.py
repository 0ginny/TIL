import cv2
import numpy as np

#caffe model 불러오기, opencv에선 많이 caffemodel이 많이 쓰여
model_name = 'res10_300x300_ssd_iter_140000.caffemodel'
prototxt_name = 'deploy.prototxt.txt'
min_confidence = 0.20
file_name= "./image/soccer_02.jpg"

def detectAndDisplay(frame):
    model = cv2.dnn.readNetFromCaffe(prototxt_name,model_name)

    blob = cv2.dnn.blobFromImage(cv2.resize(frame,(300,300)), 1.0,
                                 (300, 300) , (104.0, 177.0, 123.0)) # nomalize
    model.setInput(blob)
    detections = model.forward()

    # loop over the detections
    for i in range(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with the
        # prediction
        confidence = detections[0, 0, i, 2]

        # filter out weak detections by ensuring the `confidence` is
        # greater than the minimum confidence, 정확도 정도?
        if confidence > min_confidence:
            # compute the (x, y)-coordinates of the bounding box for the
            # object
            box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])
            (startX, startY, endX, endY) = box.astype("int")
            print(confidence, startX, startY, endX, endY)

            # draw the bounding box of the face along with the associated
            # probability
            text = "{:.2f}%".format(confidence * 100)
            y = startY - 10 if startY - 10 > 10 else startY + 10
            cv2.rectangle(frame, (startX, startY), (endX, endY),
                          (0, 255, 0), 2)
            cv2.putText(frame, text, (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # show the output image
    cv2.imshow("Face Detection by dnn", frame)


img = cv2.imread(file_name)

print(f'width : {img.shape[1]} pixels')
print(f'height : {img.shape[0]} pixels')
print(f'channels : {img.shape[2]} pixels')

(height, width) = img.shape[:2]

cv2.imshow("Original Image",img)

detectAndDisplay(img)

cv2.waitKey(0)
cv2.destroyAllWindows()