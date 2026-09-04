import torch
import torch.nn as nn
import json

torch.manual_seed(23)


embedding = nn.Embedding(5, 3)

weight = embedding.weight
with open("json_file/weight.json", "w") as f:
    json.dump(weight.tolist(), f)


input = torch.randint(0, 5, (2, 4))
input_list = input.tolist()
with open("json_file/input.json", "w") as f:
    json.dump(input_list, f)
output = embedding(input)


with open("json_file/output.json", "w") as f:
    json.dump(output.tolist(), f)

print(input)
print(output)
