import os
import shutil


def remove_cache_folders(current_repo: str = os.getcwd()) -> None:
    """Removes all __pycache__ directories in the module.

    Args:
        current_repo: current folder to clean recursively
    """
    new_refs = [current_repo + "/" + elem for elem in os.listdir(current_repo)]
    for elem in new_refs:
        if os.path.isdir(elem):
            if "__pycache__" in elem:
                shutil.rmtree(elem)
            else:
                remove_cache_folders(current_repo=elem)


if __name__ == "__main__":
    import atexit

    import torch
    import torch.nn as nn
    import torch.optim as optim
    import torchvision
    import torchvision.transforms as transforms
    from torch import Tensor

    from src.loadingpy import TrainBar

    atexit.register(remove_cache_folders)

    transform = transforms.Compose(
        [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]
    )

    batch_size = 2

    trainset = torchvision.datasets.CIFAR10(
        root="./data", train=False, download=True, transform=transform
    )
    trainloader = torch.utils.data.DataLoader(
        trainset, batch_size=batch_size, shuffle=True, num_workers=2
    )

    class Net(nn.Module):
        def __init__(self) -> None:
            super().__init__()
            self.fc3 = nn.Linear(3 * 32 * 32, 10)

        def forward(self, x: Tensor) -> Tensor:
            x = torch.flatten(x, 1)
            x = self.fc3(x)
            return x

    net = Net()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
    running_loss = torch.tensor(0.0)

    for data in TrainBar(
        trainloader,
        monitoring=running_loss,
        num_epochs=10,
        naming="loss",
        base_str="training",
    ):
        inputs, labels = data
        optimizer.zero_grad()
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss -= running_loss
        running_loss += torch.round(
            torch.tensor(loss.item(), dtype=torch.float32), decimals=3
        )

    print("Finished Training")
