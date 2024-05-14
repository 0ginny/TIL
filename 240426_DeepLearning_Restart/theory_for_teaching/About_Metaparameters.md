딥러닝은 어렵진 않지만 복잡해. 그 이유는 meta parameter들이 서로 상호 연관이 있어서 복잡하게 연관을 주고 받아.

- 기본적인 메타 파라미터들
  - Model architecture
  - number of hidden layers
  - number of units per layer
  - Cross-validataion size
  - mini-batch size
  - Activation functions
  - Optimization functions
  - learning rate
  - Dropout rate
  - Loss function
  - Data normalization
  - Weight normalization
  - Weight initaliztion
  - etc

이렇게 많기 때문에 모든 메타파라미터의 영향을 찾아볼 순 없어. 너무 오래 걸려

그래서 우리의 모델이 최고의 모델인지 확인할 수 없어.

대신 파라미터 튜닝을 통해 몇가지가 유용한 것은 알 수 있지

그래서 여러 사람들, 사이트의 코드들을 사용해보면서, 경험적으로 어떻게 해야 좋은지 유추해 볼 수 있어.