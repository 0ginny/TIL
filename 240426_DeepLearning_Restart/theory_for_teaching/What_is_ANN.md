먼저 딥러닝에 대해 설명하기 앞서, 딥러닝으로 뭘 할 수 있는지 부터 말씀드릴게요.

여러분은 무엇을 하려고 딥러닝을 배우시나요?

우선 데이터 예측을 할 수 있어요. 

만약 프로모션 데이터나, 특정 주기당 판매 데이터 같은 것들이 있다면, 
여러분은 그 데이터로 딥러닝 학습을 시켜 판매량을 예측할 수 있어요.

또 특정 제품의 불량이 있는지 확인하고 싶으면,
정상 제품 사진과, 비정상 제품 사진을 비교해서 결함을 찾을 수도 있어요.

또는 우리가 흔히 쓰는 번역기도 딥러닝으로 구현할 수 있어요.

그럼 이런 것들을 어떻게 구현하느냐?

인공지능은 우리의 신경망을 따라 만들어졌어요.

그래서 우리 신경들이 하나하나 매우 촘촘하게 연결되어 있잖아요.

딥러닝도 뉴런들이 촘촘하게 연결되어 연산을 한 값이 결국 딥러닝 모델이 되는 거에요.

그럼 그 안에선 무슨 연산을 할까요?

아주 간단하게 얘기하자면,

y = x1w1 + x2w2 

이렇게 데이터들과 가중치라는 것을 곱하고 그것들의 결과들로 예측값을 정해요.

그런데 이 예측값이 모두 하나의 뉴런에서 이뤄지고, 그 뉴런들의 예측값으로 또 다른 뉴런의 예측값이 나오고
하는 것을 반복하면서 복잡한 연산을 할 수 있는 거에요.

여기서 가장 중요한 것은 데이터는 그대로이지만, 우리가 변경해주는 건 가중치라는 거에요.

어떤 가중치를 줘야 해당 모델이 예측이나 구분을 잘하는지 찾는 것이 딥러닝 학습입니다.

사실 위처럼 단순한 구조는 쉬운 구조만 쓸 수 있어요.

예를들어 2차원 그래프에 점들이 나열되어있다고 생각해봅시다. 

이 점들 중 두 그룹이 있어서, 선을 하나 그어서 나눌 수 있으면 위의 공식을 쓰지만,

선으로 할 수 없으면 비선형으로 구분을 해야해요. 원이나, 아니면 다른 복잡한 선을 그어서 구분해야겠죠?

그런 걸 하기 위해 위 식에 비선형 함수를 곱해줘요. 그것을 활성화 함수라고 합니다.

이러한 활성화 함수 덕분에 딥러닝은 비선형 문제도 풀 수 있는 거에요.

그렇게 어려운 구조는 아니죠?

딥러닝의 종류는 ANN, CNN, RNN 등 여러가지 있는데, 모두 다 위의 구조를 기반으로 합니다. 

<hr>

이제 딥러닝 학습으로 들어가 봅시다.

지난 시간에 결국 딥러닝은 최적의 가중치를 얻는 과정이라고 했어요.

그러면 최적의 가중치는 어떻게 얻을까요??

예를 들어 샌드위치를 파는데, 최적의 양배추 양과 캐찹의 양, 계란의 굽기를 어떻게 정할까요?

단순해요. 한 번 만들고 고객에게 평가받고 고객이 만족할 때까지 만들면 되요.

그렇게 고객의 feedback을 듣고, 양배추 양을 이렇게 바꿀까? 캐찹을 이렇게 바꿀까?

하면서 가중치를 조절하는 것을 back propagation 역전파 과정이라고 합니다.

그런데 딥러닝은 이러한 층이 여러개가 있는거에요. 

그래서 가중치를 바꾸고, 그 이전 단계에도, 가중치를 바꿔달라고 요청을 하는 거죠.

그렇게 가중치를 다시 바꿨으면 다시 forward propagation을 해서 다시 고객에게 맞추는 거죠.

근데 여기서 아무런 방향없이, 무작위로 바꾸게 되면 오히려 결과가 나빠질 수도 있고,
시간이 너무 오래 걸리겠죠?

그래서 그러한 방향을 잡기위해 경사하강법이라는 것을 쓸겁니다.

미분만 알고 있으면 모두가 다 이해할 수 있어요.

다음 시간엔 간단한 수학에 대해서 배워봅시다.

<hr>

먼저 쉬어가는 시간으로 왜 요즘 사람들에게 AI가 각광받고 있을까요??

뭐가 그렇게 새로워서 그럴까요? 왜 요즘 각광받을까요?

그건 AI는 쉽기 때문입니다.

이전의 예시처럼, 판매량 예측은, 마케팅 전문가들이 있어요.

번역은 번역가들이 있지요,

요리는 맛을 잘 아는 주방장이 있을거에요.

그런데 그 사람들이 그러한 일을 하기 위해선 정말 많은 것을 배우고, 시간을 투자해야했어요.

하지만 AI는 그런 시간을 줄여주는 거죠.

사실 AI의 지능은 실증적이에요. 그러니까 원리를 모른다는 거죠.

왜 판매량이 그정도 나오는지 몰라요. 그냥 이렇게 하니까 된다. 이런 거에요.

그러니 AI를 사용한다면 원리를 알 필요가 없는거죠.

그런데 이렇게 계속 반복하기 위해선 컴퓨터 성능이 중요했어요.

그래서 컴퓨터 성능이 이제는 너무 뛰어나진 지금, 사람보다 AI가 학습하는게 더 유리해진거죠.

<hr>
<hr>

(parametic experiment?)

experimental scientist?

딥러닝 연구가는 어쩌면 실험적 과학자라 할 수 있어.

시도해보고, 결과를 시각화해서, 언제 잘 맞는지 확인을 하는거야.

여러가지 시도를 해보는 것이 중요하다 이정도로 이해할 수 있을 거 같아.
<hr>
<hr>
(강의를 시작하기 전에 뭘 배울 건지 알려주고 시작하자)
