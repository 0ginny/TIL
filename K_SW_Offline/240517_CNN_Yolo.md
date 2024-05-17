# 합성곱 신경망

convolution layer가 추가된 신경망

### 왜 써야 하는가?
이미지 데이터를 학습에 돌리기 위해 Series 형식으로 바꿔서 input 해주는데

이렇게 될 경우 제한된 데이터만 쓸 수 없어서, 차라리 이미지의 특징으로 학습을 하자는 개념에서 시작했어.

즉, 이미지 픽셀의 패턴이 중요한 것이 아니라, 이미지 특성이 중요한거야.

### 방식

- filter를 거쳐서 특징값을 구해
  - 대신 원본이미지가 소실돼.
    - 소실 시키지 않으려면 padding = 'True'
  - 얼마나 이동 시킬 것인가? stride
  - filter의 수 만큼 depth가 늘어나. 
    - 그만큼 연산양이 많아져. 
- pooling
  - 좀 흐려진 것을 선명하게? (Max poolling )
  - data 소실
- full connection

### Keras CNN parameter
