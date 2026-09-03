# Image Classification
import json
import torch
from torchvision.transforms import v2

torch.manual_seed(23)

H, W = 6, 6
img1 = torch.randint(0, 10, size=(3, 3, H, W), dtype=torch.uint8)
with open("img1.json", "w", encoding="utf-8") as f:
    json.dump(img1.tolist(), f)

# transforms = v2.RandomAffine(degrees=0, translate=(0.5, 0.5))
transforms = v2.RandomAffine(degrees=0, scale=(0.5, 0.8))

img2 = transforms(img1)

with open("img2.json", "w", encoding="utf-8") as f:
    json.dump(img2.tolist(), f)
print(img1)
print(img2)

# translate控制平移，这些像素整体会一起移动，移动后空白的像素会补0
# scale控制缩放，但不改变图像的形状，内容缩小以后，多出来的部分用0补充，内容放大之后，超出的部分会被裁掉


