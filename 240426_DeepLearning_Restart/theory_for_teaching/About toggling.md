## Training mode vs. evaluation mode

- 기울기 계산이나 평가할 땐 사용되지 않고 역전파 할 때만 사용돼.
- 정규화 방법들은 평가할 땐 사용되지 않고, 학습할 때만 사용돼.
- 그래서 실제 모델을 만들 때 평가하는 동안은 각각의 방법들이 적용되지 않도록 막아야해.

- 그 방법으로 세가지 함수를 사용할거야.
  - net.train() : training mode
  - net.eval() : testing mode
  - torch.no_grad() : used in testing mode :: grad 계산 안할 때
- 