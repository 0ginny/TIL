import cv2

# 전역 변수 초기화
start_point = None
end_point = None
cropped_image = None
image = None


# 마우스 이벤트 콜백 함수
def mouse_callback(event, x, y, flags, param):
    global start_point, end_point, cropped_image, image

    if event == cv2.EVENT_LBUTTONDOWN:
        # 마우스 왼쪽 버튼이 눌렸을 때 시작점 설정
        start_point = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        # 마우스가 움직일 때 영역 표시
        if start_point is not None:
            # 이미지 복사
            temp_image = image.copy()
            # 현재 위치와 시작점을 사용하여 영역 표시
            cv2.rectangle(temp_image, start_point, (x, y), (0, 255, 0), 2)
            cv2.imshow('Image', temp_image)
    elif event == cv2.EVENT_LBUTTONUP:
        # 마우스 왼쪽 버튼이 떼어졌을 때 종료점 설정
        end_point = (x, y)
        # 영역 잘라내기
        if start_point and end_point:
            x1, y1 = start_point
            x2, y2 = end_point
            # 좌표 정렬
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])
            # 이미지 잘라내기
            cropped_image = image[y1:y2, x1:x2]
            print(y1,y2,x1,x2)
            # 잘라낸 이미지 표시
            # 잘라낸 이미지를 저장할 파일 경로
            cropped_image_path = 'cropped_image.png'
            # 잘라낸 이미지를 파일에 저장
            cv2.imwrite(cropped_image_path, cropped_image)

            # cv2.imshow('Cropped Image', cropped_image)
            # 키 입력 대기

        # 창 닫기
        cv2.destroyAllWindows()

def main():
    global image

    # 이미지 불러오기
    image = cv2.imread('TRAIN_00071.png')

    # 창 생성
    cv2.imshow('Image', image)

    # 마우스 이벤트 콜백 함수 설정
    cv2.setMouseCallback('Image', mouse_callback)

    # # 키 입력 대기
    # cv2.waitKey(0)
    #
    # # 창 닫기
    # cv2.destroyAllWindows()
    cv2.waitKey(0)

    # 창 닫기
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
