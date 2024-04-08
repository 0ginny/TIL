# SOM
## How do Self_Organizing Maps work?

- 이전까지는 비자율 딥러닝이었어.
- 지금부터는 자율 딥러닝에 대해서 배울거야.

### SOM 이란?

 - 자율적으로 데이터를 입력받고 비슷한 그룹끼리 묶어서 정리한 것.
 - map을 통해 유사성을 알 수 있어.
 - 추가적으로 더 활용할 수 있지. (빈곤국등을 세계지도에 적용한다던지)

## K-means Clustering

- som 과 비슷한 과정
- 자율학습 알고리즘 (머신러닝 알고리즘)

### K-Means Intuition
- 간단히 말하면 복잡하게 섞인 데이터셋에서 클러스터(집단?) 을 찾아주는 알고리즘
- SOM 과 유사해

### How?
1. choose the number of K of Cluster
   - 집단을 몇개로 분류할 지 정해
2. select at random K point, the centroid
   - 아무 곳에나 집단 수만큼 랜덤으로 센터를 정해
3. Assign each data point to closet centroid -> that forms K-clusters
   - 그리고 각각 지점들을 가장 가까운 센터들의 집단에 넣어
4. compute and place the new centroid of each cluster
   - 넣어진 데이터들의 중심점으로 센터를 재설정해
5. reassign each data point to the new closest centroid, if any reassignment took place, go to Step 4, otherwise go to FIN
    - 다시 데이터들을 중심점을 기준으로 그룹화 하고 다시 센터를 재설정을 반복해.
    - 센터가 수렴하면 알고리즘 종료.
   

### Random initialization Trap

- 맨처음 초기화를 너무 이상하게 한다면 값이 달라질까?
  - 달라질 수 잇어.
- 어떻게 해결?
  - k-means++
- 사실 구분하는걸(?) 초기화 트랩을 거치는지만 알고 있으면 된대..

### choosing the right number of clusters.

- 클러스터 내 제곱합 (WCSS)
  - 각 클러스터와 중심 사의 의 거리제곱의 합의 총합.
  - 클러스터 수가 능러날만큼 WCSS는 줄어들어.
    - 최소는 0이겠지 (클러스터 수 == 데이터의 수)
  - 그러나 감소하는 폭이 매우 줄어들겠지.

#### the Elbow Method
- 팔꿈치 부분이 최적 클러스터 수.
- but 이건 참고용이고 결국엔 우리가 결정해야지.

## How do Self-Organing Maps Lern?

- ANN과 비슷해.
  - but W : features // 활성화 함수가 없어.
  - node는 마치 입력 데이터셋의 가상 공간? 임시 집합 공간? 이정도로 이해하면 될 듯.
    - k-means 했던 것처럼 센터인 것 같아.
  - 거리가 가장 짧은 노드 BMU(Best Match Unit)
  - updata
    - BMU를 기준으로 특정 범위안에 있는 지점들에 무게를 업데이트, BMU와 더 가까워지도록
      - 대신 거리가 더 가까운 지점은 더 크게 업데이트, 
    - 여러 BMU 가 있는 경우는?
      - 충돌이 발생하겠지
      - 그래도 일단 각자 센터근처의 데이터를 가깝게 가져와
      - 대신 다음부턴 점점 그 범위가 줄어들어.
        - 이렇게 되면 천천히 데이터 그룹화가 진행돼.

### Important to know
- SOMs retain topology(위상, 배치) of the input set
    - 기존 형태는 계속 유지가 된다는 거야. 대신 각 BMU쪽으로 위치가 이동하는 거지.
- SOMs reveal correctlations that are not easily identified
- SOMs classify data without supervision
  - 레이블이 필요없이 구분을 한다느 거지.
- No target vector -> no backpropaganda
- no lateral connections between output nodes.
  - 신경망연결이 수평적으로 노드가 연결되지 않아도 괜찮아.

## Live SOM example

[예시사이트_ai_junkie](http://www.ai-junkie.com/ann/som/som1.html)

## Reading an Advanced SOM

- 조직화지도는 사실 간단해 그리고 다양한 버전을 만들 수 있어.
- 그래서 해석에 의미가 있는 거야.
- 데이터를 읽는 연습을 해야해.