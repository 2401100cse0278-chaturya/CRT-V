'''
Binary Subarray
leetcode:- 930

from typing import List
def numSubarraysWithSum(nums: List[int], goal: int) -> int:
        def sub_arr(k):
            if k<0:
                return 0
            left=0
            count=0
            curr_sum=0
            for right in range(len(nums)):
                curr_sum+=nums[right] 
                while curr_sum>k:
                    curr_sum-=nums[left]
                    left+=1
                count+=(right-left+1)
            return count
        return sub_arr(goal)-sub_arr(goal-1)
nums = [1,0,1,0,1]
goal = 2
print(numSubarraysWithSum(nums,goal))


Nice Subarray
leetcode:-1248

from typing import List
def numberOfSubarrays(nums: List[int], k: int) -> int:
        def sub_arr(target):
            if target<0:
                return 0
            left,count,odd=0,0,0
            for right in range(len(nums)):
                if nums[right]%2==1:
                    odd+=1
                while odd>target:
                    if nums[left]%2==1:
                        odd-=1
                    left+=1
                count+=(right-left+1)
            return count
        return sub_arr(k)-sub_arr(k-1)
nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
print(numberOfSubarrays(nums,k))
'''

