
- np.where 은 튜플 형식으로 반환하므로 해당 값만 사용해야 할 경우 [0] 이런식으로 앞의 값만 불러와야 한다
```python
import numpy as np
import matplotlib.pyplot as plt
labels = np.zeros((n_cluster * 3, 1))
# 아래와 같이 사용해야 함.
plt.plot(data[np.where(labels == 0)[0],0],data[np.where(labels == 1)[0], 1],'bo')
# 아래와 같이 사용하면 에러발생
# plt.plot(data[np.where(labels == 0)[0],data[np.where(labels == 1)[1],'bo')
```

- tensor 로 random 한 자료배열을 만들 경우

```python
# 리스트 형으로 하려면 torch 보단 numpy로 만든 후에 tensor로 만드는 것이 더 나음.
# 만약 텐서로 할 거라면 아래와 같이 만들어야 되었음.

A = torch.vstack([a[0] + torch.randn(n_cluster) * blur, a[1] + torch.randn(n_cluster) * blur])
B = torch.vstack([b[0] + torch.randn(n_cluster) * blur, b[1] + torch.randn(n_cluster) * blur])
C = torch.vstack([c[0] + torch.randn(n_cluster) * blur, c[1] + torch.randn(n_cluster) * blur])
```


