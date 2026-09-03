import torch
import torch.nn as nn
import json

torch.manual_seed(23)

m = nn.Conv2d(3, 2, kernel_size=2)

weight_list = m.weight.detach().tolist()
bias_list = m.bias.detach().tolist()

# 保存
with open("json_file/Conv2d/weight.json", "w") as f:
    json.dump(weight_list, f, indent=4)

with open("json_file/Conv2d/bias.json", "w") as f:
    json.dump(bias_list, f, indent=4)


input = torch.randint(10, size=(1, 3, 3, 4), dtype=torch.float)

input_list = input.tolist()
with open("json_file/Conv2d/input.json", "w") as f:
    json.dump(input_list, f)

output = m(input)
with open("json_file/Conv2d/output.json", "w") as f:
    json.dump(output.tolist(), f)
