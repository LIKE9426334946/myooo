import torch


from model import resnet34

# 创建模型
model = resnet34()

# 构造输入：[B, C, H, W]
x = torch.randn(2, 3, 224, 224)

output = model(x)  # output.shape=torch.Size([2, 1000])
predicted_class = torch.argmax(output, dim=1)
print(predicted_class)

print("----")
p = torch.softmax(output, dim=1)
a, b = p.max(dim=1)
print(p)
print(a)
print(b)

print("输入形状：", x.shape)
print("输出形状：", output.shape)
