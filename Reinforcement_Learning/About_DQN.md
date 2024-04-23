# DQN(Deep-Q-Networks)

Deep learning + Q-learning

Q-Table 방식이 아닌 state를 인풋으로 DNN을 돌리는 것.

대신 정답이 없는데, 정답은 Q-Networks 공식값을 정답으로 만들어서.

장점은 state가 매우 많아도 범용적인 처리가 가능함.


## e-Greedy

강화학습에서, 최대 Q 값으로만 행동을 하면 다양성이 감소해서, local optima에 빠질 수 있음.

초반은 입실론을 크게 해서 다양하게 하다가, 학습이 진행될수록 점차 입실론을 감소시켜 수렴하도록

## Exploration and Exploitation Trade off

- Exploration : sample의 다양성을 위해 모험적인 액션 - 미래 이익을 최대화

- Exploitation : 현재 최적의 Action을 취하는 것 = 현재 이익을 최대화

- 적절한 비율로 둘을 사용해야해. 

## Replay Memory

경험을 리플레이 메모리에 저장하고, 이중 랜덤한 배치로 학습을 시켜.

학습 샘플의 다양성이 많아져.