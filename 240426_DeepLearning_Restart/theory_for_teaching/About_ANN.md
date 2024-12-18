### perceptron

ann 의 기본 구조 

y = NonLinear(xTw)

위의 모델은 bias를 넣지 않은 모델이야. 이 경우 반드시 원점을 지나야 하는 한계가 있어.

그래서 수정된 구조

y = sigma(xTw + w0)

---

가중치와 비선형함수를 사용해, 중요한 정보(일정치 이상)만을 기억하는 구조. 

#### 비선형 활성화 함수를 꼭 추가해야할까?

사실 선형적 문제에서는 오히려 활성화 함수를 추가하는 것이 더 낮은 정확도를 야기해.

그러나 현실세계에서는 비선형적인 형상의 데이터가 훨씬 많아서, 비선형적 데이터를 사용하려면 활성화 함수를 쓰는 것이 유리해.

그리고 만약 다층 모델에서 비선형 함수가 없다면, 해당 모델은 하나의 선형 모델로 변환될거야.

(xTw1)Tw2 = xTw3

그렇기 때문에 다층 구조를 쓰기 위해선 비선형 함수를 거쳐가야 해.

---

### loss function

그러면 이러한 가중치는 어떻게 변경할까?

역전파 방식을 이용해서 변경한는데,

역전파는 실제값과 예측값의 차이를 통해 경사하강법으로 가중치를 변경하는 방식이야.

그래서 우선 값의 차이를 알기위해 우리는 손실함수를 정해야해.

보통 크게 두 종류의 손실함수가 있어.


#### Mean-squared error (MSE)

연속데이터를 사용하면서 출력도 연속된 값일때.

L = 1/2 * (y_pred - y)^2

#### Cross-entropy (logistic error)

범주형 데이터를 써서 확률로 나타내는 함수

L = -(ylog(y_pred) + (1-y)log(1-y_pred))

pytorch 내에선 softmax가 같이 구현이 되어있음.

#### 추가적인 손실함수

![loss funs](./images/basic_lossfuns.png)

- KLDivLoss
  - 서로 다른 두 분포의 차이(dissimilarity)를 측정할 때 사용
  - P와 Q의 crossentropy가 같으면 최소값을 가짐

- Triplet Margin Loss

![triplet margin loss](./images/triplet_margin_loss.png)

### Cost function

이때 손실함수는 한 샘플링의 차이를 의미해. 

여기서 손실함수의 값의 평균을 구한것이 비용함수야.

J = 1/n * sum(L(y_pred_i,y_i)) = 1/n*sum(L(f(x,W)_i, y_i))

이러한 비용함수를 경사하강법을 적용할 기준 함수로 사용을 해.

#### 그럼 왜 손실함수가 아닌 비용함수가 기준이 되는가?

- 보든 샘플링마다 손실을 구하는 건 엄청난 시간적 과부하가 있고, 과적합을 야기할 수 있어.
- 그런데 여기서 너무 많은 샘플의 평균을 구하게 될 경우 민감도가 감소할 수 있어. 특히 표본 변동성이 클 경우
- 그래서 가장 좋은 방법은 샘플링 단위가 아니라 batch 단위로 비용함수를 구하는 거야. (미니배치경사하강법)

---

### 그럼 왜 아직도 통계적 방법이 많이 사용되는가??

사실 딥러닝은 최적의 값을 내는데에 적합하지는 않아.

그리고 수학적으로 뛰어나지도 않지

---

### back propergation

일단 이제부터 하나의 퍼셉트론을 unit(node) 으로 표시할거야.

그리고 이 노드들은 모두 독립적이야. 전체의 상황을 모르는 상태야.

그냥 셀 수 없이 많은 연산을 통해 예측을 하는 거야.

그러나 시대가 지나면 이것도 대체될 수도 있지
이 때, 역전파는 완전히 경사하강법과 동일하게 이루어져.

그런데 우리가 바꿀 수 있는건 w 뿐이라.

w <- w - lr*Loss_deriv (vanila gradient descent)

Loss_deriv = deriv(L(non_linear(xTw,y))

이때 Loss는 Cost로 변경되어 쓸 수 있어. 

#### 히든노드의 가중치는 어떻게 업데이트 되는가?

[참고 블로그](https://amber-chaeeunk.tistory.com/18)

역전파 과정은 chain rule로 진행돼. 각각 노드끼리의 값을 함수로 연결해서, 하나의 함성 함수로 만들고

그 함수를 각각 w_i로 편미분해서 값을 각 w_i값을 업데이트 하는 방식 

### 학습률

[학습률 비교 에니메이션 코드 github](https://github.com/pablocpz/Gradient-Descent-Visualizations)

[1D 학습률 확인용 수정 코드](https://drive.google.com/file/d/1JlDZC_SSpwTR9Z8JnR0D07Q9Zh0xoHcl/view?usp=drive_link)

학습률이 너무 높으면 아예 수렴하지 않을 수 있어. 계속 극소값 근처만 가고, 극소값 안으로 들어올 수 없으니.

그런데 차원이 증가해도 그럴까? 무수히 많은 차원에서는 어떻게 될진 모르겠다...

그래도 각각 수렴이 안될 거 같긴해.


### minibatch

미니배치란?

훈련 셋을 작은 배치로 나누는 것. 미니배치 안에 적은 수의 샘플들이 들어가는 거지.

그래서 학습할 때 전체 모델을 보여주는 것이 아니라, 미니배치 한 세트씩만 보여주는 거야.

학습을 할 때 전체 데이터로 학습하는 것보다 미니 배치로 학습하는 것이 유리해.

(추후에 업데이트 예정)

## About DL Layers

### Full connected layer

모든 이전층 노드들이 각각 해당 층 노드에 전부 연결하는 층

여기엔 가시화하지 않아도 bias가 껴있음을 인지하자.

- nn.Linear()
- keras.layers.Dense()

## About activation function

### sigmoid

이진 분류할 때 사용

- 0과 1로 구분지어줌.

### softmax

카테고리 분류할 때 사용

- 전체 합이 1이 되도록 확률로 변환해줌

## 정확도에 대해서

### 파라미터
파라미터의 영향도 매우 커

lr, hidden node, hidden layer 등 여러가지 요소들이 각각 바뀔 때마다 정확도가 달라지므로 
하이퍼 파라미터 튜닝도 매우 중요해.

#### lec 55 hidden node, epoch, learning rate
실험을 해봤을 때, hidden node, epoch 은 많을 수록 높긴 했어, 근데 시간의 문제가 있겠지?

대신 learning rate가 적합하지 않은 경우는 아예 수렴하지 않는 경우도 있어. 
optimizer가 적합하게 바꿔주긴 하겠지만, learning rate가 매우 중요해보여.

#### lec 56,57 depth and breadth
같은 노드라면 보통 wide 모델이 deep 모델보다 가중치 수가 더 많아.

##### lec 57 실험 결과
깊이가 깊다고 정확도가 오르지 않아

단순히 파라미터(weight?) 수가 많다고 정확도가 오르지도 않아.

정확도에는 여러가지가 복합적으로 적용이돼. 
예를 들어 학습률이나, 옵티마이저, 정규화 등 여러가지 사항들을 복합적으로 고려해야해.

## model 생성 방법
### Sequential
매우 쉽고 직관적이야. 

대신 만들 수 있는 모델이 한정적이지

### class(nn.Module)
Sequnetial 보다는 확실히 작성하기 불편해

하지만 만들 수 있는 모델의 한계가 없어. 무궁무진하게 만들 수 있어.