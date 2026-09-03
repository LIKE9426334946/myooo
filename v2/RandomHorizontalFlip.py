# Image Classification
import json
import torch
from torchvision.transforms import v2

torch.manual_seed(23)

H, W = 5, 5
img1 = torch.randint(0, 10, size=(3, 3, H, W), dtype=torch.uint8)
with open("img1.json", "w", encoding="utf-8") as f:
    json.dump(img1.tolist(), f)

transforms = v2.RandomHorizontalFlip(p=0.5)
img2 = transforms(img1)

with open("img2.json", "w", encoding="utf-8") as f:
    json.dump(img2.tolist(), f)
print(img1)
print(img2)
# v2.RandomHorizontalFlip(p=0.5)的意思是如果输入数据的形状是（100,3,255,255）
# 那么这100张图像要么同时翻转，要么同时不翻转。
