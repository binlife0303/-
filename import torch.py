import torch.nn as nn
from torchsummary import summary

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(1,64,kernel_size=3,stride=1, padding=1),
            nn.ReLU(),
            nn.Conv2d(64,128,kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(stride=2,kernel_size=2)
        )
        self.dense = nn.Sequential(
            nn.Linear(14*14*128, 1024),
            nn.ReLU(),
            nn.Linear(1024, 10)
        )
    def forward(self, x):
        out = self.conv(x)
        out = out.view(-1,14*14*128)
        out = self.dense(out)
        return out

model = Model()
summary(model, (1,28,28))