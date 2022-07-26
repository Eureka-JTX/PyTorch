import torchvision
from torch import nn
from torch.nn import Conv2d, MaxPool2d, Flatten, Linear, Sequential, CrossEntropyLoss
from torch.optim import SGD
from torch.utils.data import DataLoader

dataset = torchvision.datasets.CIFAR10("./dataset", train=False, transform=torchvision.transforms.ToTensor())
dataloader = DataLoader(dataset, batch_size=1)


class Eureka(nn.Module):
    def __init__(self, ):
        super(Eureka, self).__init__()
        self.model1 = Sequential(
            Conv2d(3, 32, 5, padding=2),
            MaxPool2d(2),
            Conv2d(32, 32, 5, padding=2),
            MaxPool2d(2),
            Conv2d(32, 64, 5, padding=2),
            MaxPool2d(2),
            Flatten(),
            Linear(1024, 64),
            Linear(64, 10)
        )

    def forward(self, x):
        x = self.model1(x)
        return x


eu = Eureka()
optim=SGD(eu.parameters(),lr=0.01)
for epoch in range(10):
    running_loss=0.0
    for data in dataloader:
        imgs, targets = data
        outputs = eu(imgs)
        loss = CrossEntropyLoss()
        res = loss(outputs, targets)
        optim.zero_grad()
        res.backward()
        optim.step()
        running_loss+=res
    print(running_loss)