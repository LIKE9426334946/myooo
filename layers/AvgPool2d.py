import torch
import torch.nn as nn
import json

torch.manual_seed(23)

m = nn.AvgPool2d(kernel_size=3, stride=2)
input = torch.randint(0, 10, (2, 5, 5), dtype=torch.float32)
input_list = input.tolist()
with open("json_file/input.json", "w") as f:
    json.dump(input_list, f)
output = m(input)


with open("json_file/output.json", "w") as f:
    json.dump(output.tolist(), f)
print(input)
print(output)
