"""Exercise 4.01 -- train one CNN on CIFAR-10.

Usage:   python3 main.py --net ResNet18
Writes:  results/metrics_<net>.csv   (one row per epoch)
         checkpoint/ckpt_<net>.pth   (weights from the best test-accuracy epoch)
"""
import argparse
import csv
import os

import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

from models import *  # noqa: F401,F403  (the network definitions in models/)

parser = argparse.ArgumentParser(description="CIFAR-10 training")
parser.add_argument("--net", required=True, type=str, help="network name, e.g. ResNet18")
parser.add_argument("--epochs", default=30, type=int)
parser.add_argument("--lr", default=0.1, type=float)
parser.add_argument("--batch-size", default=128, type=int)
parser.add_argument("--data-root", default="./data", type=str)
args = parser.parse_args()

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Network: {args.net} | device: {device}", flush=True)

# ---- Data -------------------------------------------------------------
mean, std = (0.4914, 0.4822, 0.4465), (0.2470, 0.2435, 0.2616)
transform_train = transforms.Compose([
    transforms.RandomCrop(32, padding=4),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize(mean, std),
])
transform_test = transforms.Compose([transforms.ToTensor(), transforms.Normalize(mean, std)])

trainset = torchvision.datasets.CIFAR10(args.data_root, train=True, download=True, transform=transform_train)
testset = torchvision.datasets.CIFAR10(args.data_root, train=False, download=True, transform=transform_test)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=args.batch_size, shuffle=True, num_workers=2)
testloader = torch.utils.data.DataLoader(testset, batch_size=100, shuffle=False, num_workers=2)

# ---- Model ------------------------------------------------------------
net = globals()[args.net]().to(device)  # looks the name up in models/
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=args.lr, momentum=0.9, weight_decay=5e-4)
scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)


def run_epoch(loader, train):
    net.train(train)
    total_loss, correct, total = 0.0, 0, 0
    with torch.set_grad_enabled(train):
        for inputs, targets in loader:
            inputs, targets = inputs.to(device), targets.to(device)
            outputs = net(inputs)
            loss = criterion(outputs, targets)
            if train:
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
            total_loss += loss.item() * targets.size(0)
            correct += outputs.argmax(1).eq(targets).sum().item()
            total += targets.size(0)
    return total_loss / total, 100.0 * correct / total  # (mean loss, accuracy in %)


# ---- Train / evaluate -------------------------------------------------
os.makedirs("results", exist_ok=True)
os.makedirs("checkpoint", exist_ok=True)
metrics_path = f"results/metrics_{args.net}.csv"
ckpt_path = f"checkpoint/ckpt_{args.net}.pth"

best_acc = 0.0
with open(metrics_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["epoch", "train_loss", "train_acc", "test_loss", "test_acc"])
    for epoch in range(1, args.epochs + 1):
        train_loss, train_acc = run_epoch(trainloader, train=True)
        test_loss, test_acc = run_epoch(testloader, train=False)
        scheduler.step()

        writer.writerow([epoch, train_loss, train_acc, test_loss, test_acc])
        f.flush()  # keep the CSV usable even if the job is interrupted
        print(f"epoch {epoch:3d}/{args.epochs} | train loss {train_loss:.4f} acc {train_acc:.2f}% "
              f"| test loss {test_loss:.4f} acc {test_acc:.2f}%", flush=True)

        if test_acc > best_acc:
            best_acc = test_acc
            torch.save({"net": net.state_dict(), "acc": test_acc, "epoch": epoch}, ckpt_path)

print(f"Done. Best test accuracy: {best_acc:.2f}%", flush=True)