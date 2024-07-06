import cv2
cap = cv2.VideoCapture()

cap.open(0, cv2.CAP_DSHOW)

while True:
    # Capture frame-by-frame
    # ret, frame = video_capture.read()
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('Video', frame)
    # q 를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()