import torch
import torch.nn as nn
import torch.nn.functional as F

identity = torch.randint(0, 10, (10, 2, 64, 64))
identity = F.pad(identity, pad=(0, 0, 0, 0, 0, 1), mode="constant", value=0.0)
identity.shape
torch.Size([10, 3, 64, 64])
