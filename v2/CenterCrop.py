# Image Classification
import json
import torch
from torchvision.transforms import v2

torch.manual_seed(23)

H, W = 6, 6
img1 = torch.randint(0, 10, size=(2, 3, H, W), dtype=torch.uint8)
with open("img1.json", "w", encoding="utf-8") as f:
    json.dump(img1.tolist(), f)

transforms = v2.CenterCrop((2, 2))
img2 = transforms(img1)

with open("img2.json", "w", encoding="utf-8") as f:
    json.dump(img2.tolist(), f)
print(img1)
print(img2)

# 所有图像都截取的是同一区域，都是中心区域
