import cv2

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# video_capture = cv2.VideoCapture(0) # 어떤 웹캠을 쓸 건지, 가장 첫번째 (내장 비디오)

# 캡쳐보드 인식
cap = cv2.VideoCapture()
# The device number might be 0 or 1 depending on the device and the webcam
cap.open(0, cv2.CAP_DSHOW)
while True:
    # Capture frame-by-frame
    # ret, frame = video_capture.read()
    ret, frame = cap.read()

    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detections = face_detector.detectMultiScale(image_gray, minSize=(100, 100),
                                                minNeighbors=5)

    # Draw a rectangle around the faces
    for (x, y, w, h) in detections:
        print(w, h)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)
    # q 를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()