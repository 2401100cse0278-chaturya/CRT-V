'''leetcode
867:Transpose Matrix

from typing import List
def transpose(matrix: List[List[int]]) -> List[List[int]]:
    r=len(matrix)
    c=len(matrix[0])
    res=[[0]* r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            res[j][i]=matrix[i][j]
    return res
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix))

566:Reshape the Matrix
'''
from typing import List
def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
        
    if m * n != r * c:
        return mat
        
    ans = [[0] * c for _ in range(r)]
        
    for i in range(m * n):
        ans[i // c][i % c] = mat[i // n][i % n]
            
    return ans
mat = [[1,2],[3,4]]
r = 1
c = 4
print(matrixReshape(mat,r,c))

