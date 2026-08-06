'''Input: nums = [1,2,3,4]
Output: [1,3,6,10]

nums=[1,2,3,4]
res=[0]*(len(nums))
for i in range(len(nums)):
    curr_sum=0
    for j in range(0,i+1):
        curr_sum+=nums[j]
    res[i]=curr_sum 
print(res)
leetcode :1732

from typing import List
def largestAltitude(gain: List[int]) -> int:
    curr_sum=0
    max_sum=0
    for g in gain:
        curr_sum+=g 
        max_sum= max(max_sum,curr_sum)
    return max_sum
gain = [-5,1,5,0,-7]
print(largestAltitude(gain))

leetcode:1991
'''
from typing import List

def findMiddleIndex(nums: List[int]) -> int:
    total=sum(nums)
    left_sum=0
    for i in range(len(nums)):
        right_sum=total-nums[i]-left_sum
        if left_sum==right_sum:
            return i
        left_sum+=nums[i]
    return -1
nums = [2,3,-1,8,4]
print(findMiddleIndex(nums))
