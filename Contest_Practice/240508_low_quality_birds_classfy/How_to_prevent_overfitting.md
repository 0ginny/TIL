출처 : <https://velog.io/@yookyungkho/%EB%94%A5%EB%9F%AC%EB%8B%9D%EC%9D%98-%EA%B3%A0%EC%A7%88%EB%B3%91-Overfitting%EA%B3%BC%EC%A0%81%ED%95%A9-%ED%95%B4%EA%B2%B0-%ED%8C%81>

1. Dropout

0.3 ~ 0.5가 기본이지만 너무 심하면 0.8도 고려가능

2. L1/L2 Regularization

가급적 출력층에 사용하는 것이 좋다.

사용법

```python
model.add(Dense(64, input_dim=100, activation='relu', kernel_regularizer=l2(0.01)))
model.add(Dropout(0.5))  # Dropout 추가
```

3. 출력층 직전의 은닉층 노드 수를 줄여라.

과적합을 막으려면 모수(parameter)수를 줄여야 해서, 은닉층을 줄이거나 은닉층 노드 수를 줄이면 좋다고 한다.

그 중 출력층 직전 은닉층 노드 수는 설명변수의 수가 되어서, 설명 변수들을 남기거나 생성하기 위해 출력직전 노드 수를 줄인다.

4. 배치정규화


+++++
- batch size는 수렴 속도랑 상관있는 거야.