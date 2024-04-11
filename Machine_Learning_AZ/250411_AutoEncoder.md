# Auto Encoders

### 직관
- 방향성 딥러닝
- 스스로를 암호화하고 복호화하는 것.
- 자율과 비자율 학습의 중간?

### 이점
- 피쳐를 알 수 있어.
- 인코딩한 후에는 히든 노드가 피쳐를 담고 있어.

### 작동방식
- [작동방식에 대한 블로그](https://probablydance.com/2016/04/30/neural-networks-are-impressively-good-at-compression/)
- 가시화노드 : 기존 평점 데이터 / 히든 노드 : 평점 데이터를 암호화 (부피가 줄어) 
  - 각각 *1, *-1 의 가중치들이 있고
  - 그러한 가중치 곱의 합이 히든 노드를 거져, 출력이 될 때 소프트맥스 함수를 돌려주면 기존 값과 동일해져.
  
### on viases
- z = f(Wx + b)
- 그냥 상수 같은 거야.
- 직관에서 점선 표현으로 보여줄거야.


## Training of an auto Encoder



## Overcomplete Hidden Layers

- what is Overcomplete?
  - if Hidden node > input nodes
    - i mean, if i need many features.
  - then, the hidden nodes can do cheat,
    - like just pass the input to output
- then how to solve this problem?
  - using below autoencoders.

## Sparse Autoencoders

각각 단계에서 은닉 층의 일부로 인코딩을 해.

이런식으로 bypass하는 걸 방지해.

## Denoising Autoencoders

입력층을 수정하여, 몇몇은 0값으로 입력하고,

역전파를 할 때는 기존 입력과 비교해.

## Cntractive Autoencoders



## Stacked Autoencoders

자동인코더에 또다른 은닉층을 만드는 것.

아래 DBN을 대체할 수 있어.

stack, RBM을 기반으로 했어.

## Deep Autoencoders

like RBM