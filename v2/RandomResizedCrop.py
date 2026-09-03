# Image Classification
import json
import torch
from torchvision.transforms import v2

torch.manual_seed(23)

H, W = 4, 4
img1 = torch.randint(0, 10, size=(3, H, W), dtype=torch.uint8)
with open("img1.json", "w", encoding="utf-8") as f:
    json.dump(img1.tolist(), f)

transforms = v2.RandomResizedCrop(size=(6, 6), scale=(0.4, 0.6))
img2 = transforms(img1)

with open("img2.json", "w", encoding="utf-8") as f:
    json.dump(img2.tolist(), f)
print(img1)
print(img2)
# 只取8个左右的元素进行resize，其它的元素不会参与运算