# Write a Python function that computes the transpose of a given matrix.

# Example:
# Input:
# a = [[1,2,3],[4,5,6]]
# Output:
# [[1,4],[2,5],[3,6]]
# Reasoning:
# The transpose of a matrix is obtained by flipping rows and columns.

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    b=[]
    for i in range (len(a[0])):
        result=[]
        for j in range (len(a)):
            result.append(a[j][i])
        b.append(result)
    return b


#tensor.t() 2-->2 dimension
#tensor.transpose(dim0,dim1) 
#permute(*dims)这个可以一次性重排所有维度顺序 高维度

#sum(len(row) for row in a) 元素总数
#