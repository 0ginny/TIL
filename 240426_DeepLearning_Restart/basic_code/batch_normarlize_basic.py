import torch
import torch.nn as nn
import torch.nn.functional as F

class ann_batch(nn.Module):
    def __init__(self):
        super().__init__()

        self.input_ = nn.Linear(11,16)

        self.bnorm1 = nn.BatchNorm1d(16)
        self.fc1 = nn.Linear(16,32)
        self.bnorm2 = nn.BatchNorm1d(32)
        self.fc2 = nn.Linear(32,20)

        self.output = nn.Linear(20,1)

    def forward(self,x):
        x = F.relu(self.input_(x))

        x = self.bnorm1(x)
        x = F.relu(self.fc1(x))

        x = self.bnorm2(x)
        x = F.relu(self.fc2(x))

        return self.output(x)