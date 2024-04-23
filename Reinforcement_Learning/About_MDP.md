# MDP(Markov Decision Process)

순차적인 의사결정 과정을 수학적으로 표현

- < S, A, P, R, r> 집합
  - S : State 집합
  - A : Action 집합
  - P : Transition Probability 행렬
  - R : Reword function
  - r : Discount Factor

- 발전 단계
- MP - MRP - MDP

- MP란? (Markov Process)
  - 상태 (s)와 사애전이 확률 로만 구성도니 환경
  - 오직 바로 이전의 상태만 고려해서 다음 확률을 구함
    - ex) 이전에 비가 얼마나 왔든지 상관없이 오늘 비왔으면 내일 맑을 확률을 구하는 느낌.
  - < S, P >

- MRP 란? (Markov Reward Process)
  - MP에서 Reward와 discount 추가
  - MP와 동일한데 각각 상태마다 reward 값이 있어서, 리워드가 커지는 방향으로 학습
  - Discount의 경우에는 나중 상태의 보상은 좀 더 낮게 평가
    - 그냥 공부보다 10일 뒤에 공부가 점수가 더 낮은 느낌?

- MDP 란?
  - MRP에 Action이 추가된 것
    - 어떤 액션을 취했을 때 리워드 값을 평가할 수 있도록
  - 중요한 내용은 어떤 상태가 좋은 상태인지, 나쁜 상태인지 이런걸 정하는 것이 어려움.

- 수학적 기초 지식
- 상태 가치 함수 (State-Value Function)
  - 상태의 좋고 나쁨을 평가
    - Determinent 상태 : 어떤 상태에서 단순 미래 리워드 값의 합
    - Non-Determinent : 어떤 상태에서 미래 리워드의 평균값의 합
- 행동 가치 함수 (Action-Value Function)
  - 어떤 상태에서 취한 행동의 좋고 나쁨을 평가
  - 상태 s 에서 어떤 행동 a를 했을 때 가치 q는 미래 보상들의 총합  

- Grid World example
  - 그리드 형태에서 강화학습을 하는 것 ex ) 미로찾기
  - 상태 가치 함수
    - 골과 가까운 상태에 높은 상태가치값
  - 행동 가치 함수
    - 골로 가까워지는 행동은 높은 상태 가치 값.

- 결론 :: 최적의 정책을 구하는 것.
  - 상태별로 어떤 선택이 최적의 경우인지.
  - 방법
    - Planing : 상태 가치 함수를 이용해 최적의 정책을 알아내는 방법
      - 환경에 대한 모델 정보를 알고 있어야해.
    - Reinforcement learning : 행동 가치 함수를 이용해 최적의 정책을 구하는 것
      - 모델 정보가 없더라도, 실제 경험을 해보며 학습을 진행할 수 있음.
      - 알고리즘 :: SARSA, Q-Learning, Rolicy Gradient