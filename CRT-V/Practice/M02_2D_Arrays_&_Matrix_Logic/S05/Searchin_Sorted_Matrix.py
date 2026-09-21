"Leetcode"
'''74. Search a 2D Matrix

from typing import List
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    m=len(matrix)
    n=len(matrix[0])
    left=0
    right=m*n-1
    while left<=right:
        mid=(left+right)//2
        row=mid//n
        col=mid%n
        if matrix[row][col]==target:
            return True
        elif matrix[row][col]<=target:
            left=mid+1
        else:
            right=mid-1
    return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix,target))


240. Search a 2D Matrix II
'''

from typing import List
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        row=0
        col=n-1
        while row<m and col>=0:
            val=matrix[row][col]
            if val==target:
                return True
            elif val>target:
                col-=1
            else:
                row+=1
        return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(searchMatrix(matrix,target))