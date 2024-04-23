## 행동 가치 함수 추정하기

행동 가치 함수를 추정하는 알고리즘.

- MC (Monte-Carlo) Method 
  - 실제 에피소드가 끝날 때까지 한 번의 경험을 수집한 뒤 해당 값으로 Q값을 갱신하는 추정 알고리즘
  - 처음을 0으로 두고, 골까지 갓을 때 거치는 횟수를 r로 곱해서 미래 가치를 얻고
  - 이런 걸 반복하면서 미래 가치의 가중치?를 정하는 알고리즘
  - 간단한 ㅁ만큼 간단한 사오항에선 잘 쓸 수 있지만, 복잡한 환경(ex 바둑)에선 사용하기 어려움.
- SARSA(State-Action-Reward-State-Action) 
  - 점진적으로 가치를 업데이트 할 수있는 알고리즘
  - 한 스텝을진행하고, 다음의 추전 Q값을 갱신  
- Q-Learning
  - SARSA오 비슷하지만, 행동을 취한 후 기존 Q값 추정치 중 max값을 정해서 다음단계로 넘어감.
  - 무한히 반복되었을 때, 최적의 Q 값임이 기존 증명되었음. 

## 용어 설명
- On-Plicy 학습
  - 지금 수집한 경험을 갠신 목표
- Off-Policy 학습
  - 지금 수집 경험 뿐 아니라 과거 나 다른 데이터에서 수집한 경험도 활용해서 학습하는 개념
- 보통 Off-Polish가 효율이 더 좋은
- SARSA : ON-policy ,Q-Learning : Off-Policy

## 알고리즘 분류
- Discrete Action Space 상황 : Q-Learning 사용
  - 에이전트가 취할 수 있는 행동이 n개중 하나로 딱 떨어지는 경우 (ex 방향이 있는 경우?)
- Continuous Action Space 상황 : Policy Gradient 사용
  - 연속된 값에서 행동을 선택해야 하는 경우, (ex 로봇팔 각도, 연속적이야)


## OpenAI Gym
  - MDP 구성으로 맵핑 라이브러리.

