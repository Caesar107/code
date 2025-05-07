# Write a Python function that computes the dot product of a matrix and a vector. The function should return a list representing the resulting vector if the operation is valid, or -1 if the matrix and vector dimensions are incompatible. A matrix (a list of lists) can be dotted with a vector (a list) only if the number of columns in the matrix equals the length of the vector. For example, an n x m matrix requires a vector of length m.

# Example:
# Input:
# a = [[1, 2], [2, 4]], b = [1, 2]
# Output:
# [5, 10]
# Reasoning:
# Row 1: (1 * 1) + (2 * 2) = 1 + 4 = 5; Row 2: (1 * 2) + (2 * 4) = 2 + 8 = 10

import torch
from typing import Union

def torchversion(a: list[list[Union[int, float]]], b: list[Union[int, float]]) -> list[float]:
    if len(a[0]) != len(b):
        return -1
    result = []
    for i in range(len(a)):
        row_tensor = torch.tensor(a[i], dtype=torch.float32)
        b_tensor = torch.tensor(b, dtype=torch.float32)
        result.append(torch.dot(row_tensor, b_tensor).item())
    return result

def normalversion(a: list[list[Union[int, float]]], b: list[Union[int, float]]) -> list[float]:
    if len(a[0]) != len(b):
        return -1
    return [sum(a[i][j] * b[j] for j in range(len(b))) for i in range(len(a))]

# 用户选择部分
print("Input whether torch is allowed (1 for yes, 0 for no):")
judge = input()

# 定义示例数据
a = [[1, 2], [2, 4]]
b = [1, 2]

# 根据用户选择调用不同版本
if judge == "1":
    result = torchversion(a, b)
else:
    result = normalversion(a, b)

print("Result:", result)



#torch.dot() 只接受两个 一维向量，不能处理二维矩阵
