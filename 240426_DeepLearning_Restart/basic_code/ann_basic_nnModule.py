import numpy as np
import torch
import torch.nn as nn
import torch.nn.funtional as F
import matplotlib.pyplot as plt



# create data
a = [0,0]
b = [4,0]
n_cluster = 100
blur

A = [a[0]+blur * np.random.randn(n_cluster),
     a[1]+blur * np.random.randn(n_cluster)]
B = [b[0]+blur * np.random.randn(n_cluster),
     b[1]+blur * np.random.randn(n_cluster)]

data_np = np.hstack((A,B)).T
data = torch.tensor(data_np).float()

labels_np = np.vstack(np.zeros(n_cluster,1),np.ones(n_cluster,1))
labels = torch.tensor(labels_np).float()

plt.figure(figsize = (5,5))
plt.plot(data[np.where(labels == 0)[0],0],
         data[np.where(labels == 0)[0],1],
         'bo')
plt.plot(data[np.where(labels == 1)[0],0],
         data[np.where(labels == 1)[0],1],
         'ro')
plt.show()


class ANN(nn.Module):
    # create objects
    def __init__(self):
        self.input_ = nn.Linear(2,1)
        self.output_ = nn.Linear(1,1)
    # action when model is called
    def forward(self,x):
        x = self.input_(x)
        x = F.relu(x)
        x = self.output(x)
        x = torch.sigmoid(x)

        return x

ann = ANN() # __init__

# compile
learningRate = .01
lossfun = torch.BCELoss()
optimizer = torch.optim.SGD(ann.parameters(),lr= learningRate)

# training
epochs = 500

for epoch in range(epochs):
    yhat = ann(data) # forward

    loss = lossfun(yHat,labels)

    # backpropergation
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# validataion
prediction = ann(data)
predlabels = prediction > .5

## find errors
misclassified = np.where(predlabels != labels)[0]

## total accuracy
totalacc = 100-100*len(misclassified)/(2*nPerClust)

print(f'Accuracy : {totalacc}')