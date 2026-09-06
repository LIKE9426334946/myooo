import torch
import torch.nn as nn
import torch.nn.functional as F

torch.manual_seed(23)
m = nn.BatchNorm2d(3, affine=False)
input = torch.randint(0, 10, size=(1, 3, 5, 5), dtype=torch.float32)
output = m(input)

a1 = torch.mean(input, dim=(0, 2, 3))
a2 = torch.std(input, correction=0, dim=(0, 2, 3))
print(f"{input=}")
print(f"{output=}")
print(a1, a2)
