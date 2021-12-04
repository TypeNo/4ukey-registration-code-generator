import torch
from torch.utils.data import dataloader
from model.malexnet import mAlexNet
from model.alexnet import AlexNet

import torchvision
from torchvision import transforms
from torchvision import models

import matplotlib.pyplot as plt

from PIL import Image

from utils.dataloader import selfData, collate_fn
from torch.utils.data import Dataset, DataLoader

def test(net, transforms, img_path='CNRPark-Patches-150x150/', target_path='splits/CNRParkAB/odd.txt'):
    print("\nTesting starts now...")
    test_dataset = selfData(img_path, target_path, transforms)
    test_loader = DataLoader(test_dataset, batch_size = 100, shuffle = True, num_workers = 0, collate_fn=collate_fn)
    correct = 0
    total = 0
    item = 1

    with torch.no_grad():
        for data in test_loader:
            images, labels = data
            print("Testing on batch {}".format(images))
            labels = list(map(int, labels))
            labels = torch.Tensor(labels)
            if torch.cuda.is_available():
                device = torch.device("cuda:0")
                images = images.to(device)
                labels = labels.to(device)
            print(images)
            outputs = net(images)
            print(outputs)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
            item += 1
    return (correct/total)

PATH = 'model.pth'
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.RandomResizedCrop(224),
    transforms.ToTensor(),  # normalize to [0, 1]
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
]) 
img = Image.open("pklot1.jpg")
net = mAlexNet().to(device)

def load_model():
    print("\nTesting starts now...")
    model = mAlexNet().to(device)
    # model = net = AlexNet().to(device)
    model.load_state_dict(torch.load(PATH))
    print(model)

    model.eval()
    # img1 = img.crop((762, 418, 812, 483))
    img1 = img.crop((719, 417, 762, 481))

    img_t = transform(img1)
    batch_t = torch.unsqueeze(img_t, 0)
    print(batch_t)
    out = model(batch_t)

    # img1.show()
    print(out.shape)

    _, indices = torch.max(out, 1)
    percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
    print(percentage[indices[0]].item())

    print(indices[0].numpy())


if __name__=="__main__":
    load_model()