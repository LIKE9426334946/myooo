import torch
import json

x = torch.randint(10, (2, 3))
x1 = torch.randint(10, (2, 3))
x2 = torch.stack([x, x1])

x = x.detach().tolist()
with open("demo.json", "w", encoding="utf-8") as f:
    json.dump(x, f)

x1 = x1.detach().tolist()
with open("demo1.json", "w", encoding="utf-8") as f:
    json.dump(x1, f)

x2 = x2.detach().tolist()
with open("demo2.json", "w", encoding="utf-8") as f:
    json.dump(x2, f)
