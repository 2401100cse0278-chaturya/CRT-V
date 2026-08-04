'''209. Minimum Size Subarray Sum

from typing import List
def minSubArrayLen(target: int, nums: list[int]) -> int:
    left = 0
    current_sum = 0
    min_length = float('inf')
    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
    return min_length if min_length != float('inf') else 0
target=7
nums=[2,3,1,2,4,3]
print(minSubArrayLen(target,nums))

713. Subarray Product Less Than K

from typing import List
def numSubarrayProductLessThanK(nums: List[int], k: int) ->int:
    if k<=1:
        return 0
    left=0
    c=0
    p=1
    for right in range(len(nums)):
        p *= nums[right]
        while p>=k:
            p//=nums[left]
            left+=1
        c+=(right-left+1)
    return c
nums = [10,5,2,6]
k = 100
print(numSubarrayProductLessThanK(nums,k))

904. Fruit Into Baskets

from typing import List
def totalFruit(fruits: List[int]) -> int:
    left=0
    ans=0
    freq={}
    for right in range(len(fruits)):
        freq[fruits[right]]=freq.get(fruits[right],0)+1
        while len(freq)>2:
            freq[fruits[left]] -=1
            if freq[fruits[left]]==0:
                del freq[fruits[left]]
            left+=1
        ans=max(ans,right-left+1)
    return ans
fruits = [1,2,1]
print(totalFruit(fruits))
'''