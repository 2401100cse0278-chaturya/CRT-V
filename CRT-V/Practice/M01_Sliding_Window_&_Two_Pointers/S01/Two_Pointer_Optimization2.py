'''
#Leetcode Problems
26.Remove Duplicates from Sorted Array
from typing import List
def removeDuplicates(nums: List[int]) -> int:
    i=0
    for j in range(1,len(nums)):
        if nums[i]!=nums[j]:
            i=i+1
            nums[i]=nums[j]
                
    return i+1
nums=[0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))

27.Remove Element


from typing import List
def removeElement(nums: List[int], val: int) -> int:
    k=0
    for i in range(0,len(nums)):
        if nums[i]!=val:
            nums[k]=nums[i]
            k+=1
    return k
nums=[0,1,2,2,3,0,4,2]  
val=2
print(removeElement(nums,val))         

167.Two Sum II - Input Array Is Sorted

from typing import List
def twoSum(numbers: List[int], target: int) -> List[int]:
    left=0
    right=len(numbers)-1
    while left<right:
        total=numbers[left]+numbers[right]
        if total==target:
            return [left+1,right+1]
        elif total>target:
            right-=1
        else:
            left+=1
numbers=[2,7,11,15]
target = 9
print(twoSum(numbers,target))

977. Squares of a Sorted Array

from typing import List
def sortedSquares(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        nums[i]=nums[i]*nums[i]
    nums.sort()
    return nums
nums = [-7,-3,2,3,11]
print(sortedSquares(nums))
      '''  