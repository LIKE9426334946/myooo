import torch
import torch.nn as nn

m = nn.Conv1d(3, 2, 2)
m.weight
m.bias

input = torch.randn(2, 3, 4)

output = m(input)
