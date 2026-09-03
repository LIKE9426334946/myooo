# Image Classification
import json
import torch
from torchvision.transforms import v2

torch.manual_seed(23)

H, W = 4, 4
img1 = torch.randint(0, 255, size=(2, 3, H, W), dtype=torch.uint8)
with open("img1.json", "w", encoding="utf-8") as f:
    json.dump(img1.tolist(), f)

transforms = v2.ToDtype(torch.float32)

img2 = transforms(img1)

with open("img2.json", "w", encoding="utf-8") as f:
    json.dump(img2.tolist(), f)
print(img1)
print(img2)
