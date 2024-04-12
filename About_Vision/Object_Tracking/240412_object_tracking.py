import cv2

# create tracker
tracker = cv2.TrackerKCF_create()

video = cv2.VideoCapture('race.mp4')

# read first Frame
ok, frame = video.read()

# 맨처음 추척할 객체 찾기기
bbox = cv2.selectROI(frame)
# x, y, w, h
# print(bbox)

ok = tracker.init(frame, bbox)
print(ok)

# 전체 프레임으로 추적.
while 1 :
    ok, frame = video.read()
    if not ok : # 객체를 높지면 break
        break
    # 객체 위치 update
    ok, bbox = tracker.update(frame)


    # draw box
    if ok :
        (x,y,w,h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x,y), (x+w, y+ h),
                      (0, 255,0), 2, 2)
    else :
        cv2.putText(frame, 'Error', (100, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0XFF == 27 : # press ESC
        break