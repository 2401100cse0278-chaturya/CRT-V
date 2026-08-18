'''Leetcode:
1572. Matrix Diagonal Sum

from typing import List
def diagonalSum(mat: List[List[int]]) -> int:
    n=len(mat)
    s=0
    for i in range(n):
        for j in range(n):
            if i==j:
                s+=mat[i][j]

            if i+j==n-1:
                s+=mat[i][j]
    if n%2==1:
        s-=mat[n//2][n//2]
    return s
mat = [[1,2,3],
      [4,5,6],
      [7,8,9]]
print(diagonalSum(mat))

498. Diagonal Traverse
'''
from typing import List

def findDiagonalOrder(mat: List[List[int]]) -> List[int]:
    rows=len(mat)
    cols=len(mat[0])
    res=[]
    for d in range(rows+cols-1):
        diagonal=[]
        if d<cols:
            r=0
            c=d
        else:
            r=d-cols+1
            c=cols-1
        while r<rows and c>=0:
            diagonal.append(mat[r][c])
            r+=1
            c-=1
        if d%2==0:
            res.extend(reversed(diagonal))
        else:

            res.extend(diagonal)
    return res
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(findDiagonalOrder(mat))

'''1380 : Lucky Numbers in a Matrix

from typing import List
def luckyNumbers(matrix: List[List[int]]) -> List[int]:
    row_mins = {min(row) for row in matrix}
    col_maxs = {max(col) for col in zip(*matrix)}
    return list(row_mins & col_maxs)
matrix = [[3,7,8],[9,11,13],[15,16,17]]
print(luckyNumbers(matrix))

1582 : Special Positions in a Binary Matrix
'''
from typing import List
def numSpecial(mat: List[List[int]]) -> int:
    m, n = len(mat), len(mat[0])
    row_sum = [sum(row) for row in mat]
    col_sum = [sum(col) for col in zip(*mat)]
    special_count = 0
    for r in range(m):
        for c in range(n):
            if mat[r][c] == 1 and row_sum[r] == 1 and col_sum[c] == 1:
                special_count += 1
                    
    return special_count
mat = [[1,0,0],[0,0,1],[1,0,0]]
print(numSpecial(mat))