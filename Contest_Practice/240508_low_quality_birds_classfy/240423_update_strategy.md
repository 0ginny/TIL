
### updated 240423

1. 전이학습
- 모델별로 전이학습만 해서 최적의 모델 선정
  - keras : Xception
  - hugging face : swin v2

2. 파인튜닝
- 얼마나 파인튜닝하면 좋을지 선정

3. 업스케일 이용.
- imageDataGenerater를 이용해서 dataset 만들고
- 아래의 코드를 사용해서, image와 label 분리
```python
    # 이미지 데이터만 추출
for i in range(len(generator)):
    batch = generator.next()  # 다음 데이터 배치 가져오기
    images = batch[0]  # 이미지 데이터만 추출
    # 여기에서 이미지 데이터에 대한 추가 처리 수행
```

- 이미지 업스케일 후 해당 데이터로 파인튜닝 진행. 