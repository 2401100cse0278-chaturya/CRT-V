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


