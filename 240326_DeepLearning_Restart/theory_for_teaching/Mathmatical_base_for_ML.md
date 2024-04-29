우리가 머신러닝 수학을 공부할 방법은 spectral teories 야.

이 말은 하나의 개념에서 시작해서, 그 개념을 잘게 부숴서 독립 개별 개념으로 이해할 거라는 거지.

딥러닝은 간단하지만 complicated, complex 한 내용이야.

complicated는 부품이 많지만, 어렵지는 않아. 단순하게 이해하고 사용할 수 있어. 직관적이야.

이와 비교해서 complex는 수는 덜 하지만, 비선형적이고, 이해하기가 어려운 내용을 의미하지.  

정리하자면,

사실 딥러닝은 매우 쉬운 수학적 개념으로 만들어졌어. 가중치를 데이터와 곱해서 더한다.라는

그러나 매우 많은 파트들의 결합으로 complicated 하고

비선형적 구조를 보면 이해할 수 없을 정도로 complex하기도 해.

---
---
(이번시간에는 머신러닝에 대한 수학적 이해를 위해 우리끼리 사용할 용어 정리를 하고 넘어가겠습니다.)

우선  ML에서 사용되는 자료구조 부터 이해하고 넘어갑시다.

완전히 정확한 개념은 아니지만 ML을 하면서 소통이 될 수만 있도록 이해하고 갈게요.

먼서 Scalar 는 단순한 숫자라고 생각하면 됩니다. 

다음으로는 Vector 는 숫자의 열 혹은 행 정도로 이해하면 되고,

Matrix는 그러한 행과 열이 합쳐져서 2차원 행렬이 될 때를 지칭할게요.

마지막으로 우리가 주로 사용할 Tensor는 3차원 이상의 배열들을 표현할 때 사용하겠습니다.

추가적으로 우리는 np.array와 torch.tensor 라는 타입을 쓸건데, 
이러한 데이터 타입의 개념을 자세히 알기보다는, 
데이터 타입이 다르면 작동되지 않을 수 있다는 사실만 기억하시고,
코드 작성시 유의해주세요. 

---

다음으로 우리가 다룰 데이터의 두 성질에 대해서 간단히 집고 넘어갑시다.

continuous와 categorical 성질이 있는데요.

continuous는 연속적인 성질, 숫자 성질이라고 이해하시면 되요. 거의 무한한 데이터를 구분할 수 있지요.

categorical은 목차가 있는 성질이라고 보시면 됩니다. 분류를 위한 데이터로 맞는지, 아닌지를 구분하는 데이터라고 생각하시면 됩니다.

그러나 ML을 하면서 문자열 데이터는 사용하기 매우 불편합니다. 그래서 categorical 데이터를 encoding해서 주로 쓰는데요.

labelencoding과 onehotencoding을 주로쓰는데 이에 대해선 실습에서 설명해드리겠습니다.

---

다음으로 전치(Transpose)에 대해서 간단히 설명해드릴게요

우리가 ML에선 데이터에 가중치를 곱해준다고 했잖아요? 근데 하나하나 곱하게 되면 너무 귀찮잖아요.

그래서 행렬의 내적(dot product)으로 한번에 곱하는 방법을 사용해요.

그런데 이 내적을 위해선 행렬의 크기가 조정이 되야 하는데요.

만약 m x n 크기의 행렬에 내적을 해주려면 n x ? 의 행렬만 곱할 수 있어요.

그래서 m x n 행렬에 m x n 행렬을 곱하려면 n x m 으로 형태를 바꿔줘야 하는데 

그 방법이 전치 입니다.

단순히 행과 열만 바꿔주면 되요.

그리고 우리는 전치 transpose의 앞 글자를 따서 T 를 붙여서 표시하겠습니다.

```python
# numpy
import numpy as np

np.array.T
np.transpose()

# pytorch
torch.tensor.T

```

그래서 다음으로 dot product 가 어디에 쓰이는지 확인하자면

ann 에선 이전에 말했듯이 가중치 벡터와 데이터 벡터를 곱해서 하나의 스칼라 값을 낼 수 있습니다.

그리고 이후 이미지 분류에 사용되는 CNN 에서 Convolution 이라는 개념이 나오는데,

그 때 우리의 2차원 데이터와 convoulution layer의 filter로 값을 내적해줘서,

복잡한 이미지 데이터에서 특징 데이터를 추출할 수 있습니다.

수학적으로 보자면 두 값 사의의 상관관계를 숫자로 표현했다고 이해하면 될 거 같습니다.

```python
# numpy
np.dot(nv1, nv2)
# np.sum(nv1 * nv2) 와 결과가 같아
nv1 @ nv2

# pytorch
torch.dot(tv1, tv2)
torch.sum(tv1 * tv2)
```

다음으로 우리가 사용할 활성화 함수에 대해 몇가지 중요한 것들만 소개할게요.

첫번째로 softmax 함수가 있습니다.

이 함수는 카테고리 분류할 때 많이 쓰이는데요.

그 이유는 이 함수의 결과는 각 요소의 합이 1인 벡터로 나오기 때문입니다.

그래서 예측값이 원숭이 인지 강아지인지, 고양이인지 확률로 나타내 줄 수 있는 함수입니다.

예를들어 딥러닝의 결과로 [20, -21, 2, 5] 이런 결과가 나왔을 때,

이러한 단순한 숫자를 확률로 나타내 줄 수 있는 함수입니다.

```python
import numpy as np

num = np.exp(nv)
den = np.sum(np.exp(nv))
sigma = num /den

import torch as nn
softfun = nn.Softmax(dim = 0)
sigmaT = softfun(torch.Tensor(nv))
```
---
---
_딥러닝에서 log 함수로 손실을 계산하는데, 그 이유는 어차피 log 값이 작으면 해당 값도 작은데,
심지어 변화폭이 기하급수적으로 작아서 계산하기 용이하기 때문에_
---
---
_엔트로피에 대해서, 데이터 공학 쪽에선, 높은 엔트로피는 해당 데이터셋이 많은 가변성을 가지고 있다는 의미이고,
낮은 엔트로피는 대부분의 값들이 반복되고 고착화 된다는 의미야._

_엔트로피와 균등분배Variance?에 대해선, 엔트로피는 비선형값이고, 분배에 대한 가정치?가 없는데 반해
균등분배는 효율성에 기준을 두고 일반 대이터를 대강 가정하는 거야. 매우 복잡하구먼_

_entropy :: H(p,q) = - sum(plog(p)) :: 
한 요소의 분배 확률을 나타내_

_crossentropy :: H(p,q) = - Sum(plog(q)) :: 
두 분배 가능성에 대한 관계를 나타내_

```python
# 확률은 가능한 확률가 가능하지 않은 확률 둘 다 있는 거야. softmax와 잘 어울리네
import numpy as np
P = [.25, .75]
H = 0
# calculate entropy / len(P) == 2 ,binary cross entropy
for p in P:
    H -= p * np.log(p)

# cross entropy
# p와 q 위치를 바꾸면 값이 달라져.
P = [1.0, 0.0000000001]
Q = [.25, .75]
for i in range(len(P)):
    H -= P[i]* np.log(Q[i])
# binary cross entropy
# P[1] << 0
H = -np.log(Q[0])

import torch 
# pytorch
torch.nn.functional.F.binary_cross_entropy(torch.tensor(Q),torch.tensor(P))

```
---
---

_Tip. softmax의 최고 확률값을 알고 싶을 때, argmax() 사용_

```python
import numpy as np
np.argmax(X)
np.argmax(X,axis = 0)

import torch
min = torch.min(X)
min2 = torch.min(X,axis = 0)
min2.values # min
min2.indices #argmin
```
---
---
분산(variance)과 표준 편차(standard variance)에 대해선 L1, L2 정규화할 때 사용할 거야.
```python
var1 = np.var(X)
var2 = (1/(n-1)) * np.sum((x-mean) ** 2)
# 값이 다를거야. 그이유는 편향때문에.
# var1 = (1/(n)) * np.sum((x-mean) ** 2)
# 그래서 편향이 있어.
# 정확한 값
var3 = np.var(X, ddof = 1)
# 그러나 사실 데이터 수가 커지면 큰 차이는 없어.


```
---
---
딥러닝에는 왜 많은 양의 데이터가 필요할까??

random sampling에 대해서

sampling variability (표본 가변성) 때문인데, 표본이 달라지면 평균같은 특징 데이터도 달라지기 때문이야.

그래서 단순 전체를 이해하기 위한 샘플링 측정이 한 번이면, 신뢰도할 수 없지.

표본 가변성은 아래와 같은 요인들에 의해 생겨

- 자연적 가변 : 모든 개체가 같을 순 없으니,
- Measurement noise : 측정 센서가 완전히 정확할 수 없어
- Complex system : 생태계나 시스템은 하나의 요인이 결정하는 것이 아니라 무수히 많은 변수들이 영향을 주고받고 있어.

이 표본 변동성은, 모집단이 커질 수록, 뽑는 표본의 수가 클 수록 전체 평균에 근사하겓 돼

---
---

이러한 변동성 때문에 실험을 할때 값이 달라질거야.

그래서 python에서 seeding을 통해 변동성을 고정할수 있어.

```python
np.random.seed(42)

randseed = np.random.RandomState(42)

randseed1.randn(5)
randseed1.randn(5)
#  이 둘 값은 달라, 근데 이 코드를 반복하면 이전과 같은 값을 얻을 수 있어.
# 이렇게 재현은 가능하지만 랜덤 값이 달라지게 하는 상황이 있을 수있어서. 더 많이 쓰여

torch.manual_seed(42)
```

---
---

그럼 변동성이 있는지 없는지는 어떻게 판단할까?

그 방법으로 t-test를 할 수 있어

두 샘플링 된 데이터가 '평균적'으로 비슷한가를 판단하는 방법으로 t-test를 사용해.

t-value = (Difference of means) / (standard deviations)

t-value가 크면 두 표본의 평균차가 큰 것이고, 작으면 표본의 평균차가 작은 거야.


```python
import numpy as np
import matplotlib.pyplot as plt

import scipy.stats as stats

stats.ttest_ind(data2,data1)
```

+++ 그 일이 실제 일어날 확률을 나타낸 지표 p-value

확률밀토 함수에서 특정 값 이상 혹은 이하의 넓이로, 확률을 나타내어, 통계적 결과의 신뢰성을 보여주는 값.

그래서 확률밀도 함수에서 t-test로 t-score(value)를 얻고, 그 이상, 이하 값으로 p-value를 얻어서 신뢰도를 알 수 있어.

p-value가 낮을 수록 그 표본의 신뢰도가 높다는 의미, 

p-value는 샘플링 데이터가 우연히 일어날 확률을 의미

[p_value blog](https://justdoitman.tistory.com/51)

---
---

미적분에 대해서, 딥러닝에서 미적분을 배워야하는 이유는,

일단 딥러닝이 하는 일은 분류야. 옳은가 옳지 않은가를 분류하는 거야.

그래서 옳지 않으면 옳은 방향으로 움직여야되겠지?

그래서 그 옳은 방향을 알기 위해 미분을 사용하는 거야.

---
---

그럼 미분으로 방향을 정할때 기준은 어떻게 될까?

우리가 하고 싶은 건 실제값과 예측값의 차이가 가장 작기를 원하잖아?

그러면 최소값을 얻어야 겠지?

최소값은 극값에서 이루어져. 그리고 극값은 미분값이 0일때지

극대값과, 극소값이 있는데, 극소값은 미분값이 d < 0 -> d == 0 -> d > 0 의 값을 가져

그래서 이 조건을 만족하는 값으로 방향을 바꿔주는거야.

그런데, 저러한 형상을 보이지만 극값이 아닌 경우도 있어.

---
---

product rul of deriatives :: chain rule

마지막으로 방향을 구할 때, 쉬운 함수는 그냥 미분을 하면 되지만, 

여러 함수가 합쳐진 경우 합성곱 미분을 해야해. 