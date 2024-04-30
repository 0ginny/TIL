import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

N = 30
x = torch.randn(N,1)
y = x + torch.randn(N,1)/2

# build basic ann model
ANNreg = nn.Sequential(
    nn.Linear(1,1), # input layer
    nn.ReLU(), # 활성화 함수
    nn.Linear(1,1) # output layer
)

learningRate = .5

# 손실 함수
lossfun = nn.MSELoss()

# optimizer
# 우리가 사용할 경사하강법의 방법을 결정하는 거라고 보면 돼.
optimizer = torch.optim.SGD(ANNreg.parameters(),
                            lr = learningRate)

# start train

numepochs = 100
losses = torch.zeros(numepochs)

for epoch in range(numepochs):

    # model prediction
    yHat = ANNreg(x)

    # compute loss
    loss = lossfun(yHat,y) # 예측값과 비교값 입력
    losses[epoch] = loss # loss 저장

    # pack propergation # 나중에 이어서
    optimizer.zero_grad() # 일단 옵티마이저를 초기화해야해??
    loss.backward()
    optimizer.step()

# 학습후 검증
prediction = ANNreg(x)

# 수동으로 MSE 구하기
testloss = (prediction - y).pow(2).mean()

'''
이때 testloss 는 tensor 값이야. 
값만 얻고 싶을 땐
testloss.detach()
testloss.item()
이렇게 하면 불필요한 정보를 차단할 수 있어.
'''

# 수치 그래프화
plt.plot(x,y, 'bo', label = 'Real data')
plt.plot(x,prediction.detach(),'rs',label = 'Predictions')
plt.title(f'prediction-data r = {np.corrcoef(y.T, prediction.detach().T)[0,1]:.2f}')
plt.legend()
plt.show()