import torch
import torch.nn as nn

m = nn.Conv1d(3, 2, 2)
m.weight
m.bias

input = torch.randn(2, 3, 4)

output = m(input)
a1 = np.random.randint(0, 10, (2, 3, 4))


a2 = np.random.randint(0, 10, (2, 4, 3))

c = np.matmul(a1, a2)

a = torch.randn(2, 3, 4)
b = torch.randn(2, 4, 3)
