#### pytorch parameter에 대해서
```python
# import libraries
import numpy as np
import torch
import torch.nn as nn

deepnet = nn.Sequential(
    nn.Linear(2,2),  # hidden layer
    nn.Linear(2,2),  # hidden layer
    nn.Linear(2,3),  # output layer
    )

# check out the parameters
for p in deepnet.named_parameters():
  print(p)
  print(' ')

# count the number of nodes ( = the number of biases)

# named_parameters() is an iterable that returns the tuple (name,numbers)
numNodesInDeep = 0
for paramName,paramVect in deepnet.named_parameters():
  if 'bias' in paramName:
    numNodesInDeep += len(paramVect)
print('There are %s nodes in the deep network.' %numNodesInDeep)
```