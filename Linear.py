import torch
import torch.nn as nn
import json

torch.manual_seed(23)


m = nn.Linear(3, 5)

weight_list = m.weight.detach().tolist()
bias_list = m.bias.detach().tolist()

# 保存
with open("json_file/Linear/weight.json", "w") as f:
    json.dump(weight_list, f, indent=4)

with open("json_file/Linear/bias.json", "w") as f:
    json.dump(bias_list, f, indent=4)

input = torch.randint(10, size=(2, 3), dtype=torch.float)

input_list = input.tolist()
with open("json_file/Linear/input.json", "w") as f:
    json.dump(input_list, f)

output = m(input)
with open("json_file/Linear/output.json", "w") as f:
    json.dump(output.tolist(), f)
