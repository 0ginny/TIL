# 데이터 정규화

딥러닝을 할 때, 각각의 칼럼들마다 통계적 배치가 다를거야.

그 상태로 딥러닝을 하면, 가중치의 곱으로 손실이 계산되기 때문에, 상대적으로 높은 수의 영향이 커질 수 밖에 없어.

그래서 통계적으로 같은 범위에 놓기 위해서 데이터 정규화를 진행해야해.

### 방식

- z-nomalization(transform)
  - Zi = (xi - x_mean) / x_standard
  - 데이터의 숫자는 변하지만, 데이터의 통계적 형상은 변하지 않아.
  - 일반적인 분포 데이터에서 사용

```python
import scipy.stats as stats
import pandas as pd
iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

cols2zscore = iris.keys()
cols2zscore = cols2zscore.drop('species')
iris[cols2zscore] = iris[cols2zscore].apply(stats.zscore)
```

- min-max-scaling
  - 큰 값이 1, 최소값이 0 으로
  - x~ = (x- x_min) / (x_max - x_min)
  - 만약 a 에서 b 범위로 스케일하고 싶으면
    - x* = a + x~(b-a)
  - 이미지 처리나, uniform 데이터에서 주로 사용돼