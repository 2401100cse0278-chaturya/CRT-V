'''
leetcode:- 48

from typing import List
def rotate(matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(0,n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for row in matrix:
            row.reverse()
        return matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))



leetcode:- 1886
'''
from typing import List
def findRotation(mat: List[List[int]], target: List[List[int]]) -> bool:
        n=len(mat)
        for _ in range(4):
            if mat==target:
                return True
            mat.reverse()
            for i in range(0,n):
                for j in range(i+1,n):
                    mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
        return False
mat = [[0,1],[1,0]]
target = [[1,0],[0,1]]      
print(findRotation(mat,target))