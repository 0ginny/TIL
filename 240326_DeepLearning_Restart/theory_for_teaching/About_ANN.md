### perceptron

ann 의 기본 구조 

y = NonLinear(xTw)

위의 모델은 bias를 넣지 않은 모델이야. 이 경우 반드시 원점을 지나야 하는 한계가 있어.

그래서 수정된 구조

y = sigma(xTw + w0)