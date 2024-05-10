import numpy as np
from torch.utils.data import DataLoader, TensorDataset

# create our fake dataset

fakedata = np.tile(np.array([1,2,3,4]),(10,1)) + np.tile(10*np.arange(1,11),(4,1)).T
fakelabels = np.arange(10)>4
print(fakedata), print(' ')
print(fakelabels)

# 데이터와 라벨을 합쳐 데이터셋 생성
fakeDataset = TensorDataset(torch.Tensor(fakedata),torch.Tensor(fakelabels))
print( fakeDataset.tensors ), print(' ')

# 데이터셋 가공?
fakedataLdr = DataLoader(fakeDataset, batch_size = 2, shuffle=True)

# check data
for dat,lab in fakedataLdr:
  print(dat,lab)