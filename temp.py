import torch
import torch.nn as nn
import json

torch.manual_seed(23)
import numpy as np

np.random.seed(23)

a1 = np.random.randint(0, 10, (2, 5))


a2 = np.random.randint(0, 10, (5))

c = np.matmul(a1, a2)
print(c.shape)
b1 = a1.tolist()
b2 = a2.tolist()
c = c.tolist()


print(f"b1={b1}")
print(f"b2={b2}")
print(f"c={c}")
with open("json_file/test1.json", "w") as f:
    json.dump(b1, f)

with open("json_file/test2.json", "w") as f:
    json.dump(b2, f)

with open("json_file/test3.json", "w") as f:
    json.dump(c, f)
