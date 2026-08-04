'''1493. Longest Subarray of 1's After Deleting One Element
from typing import List
def longestSubarray(nums: List[int]) -> int:
    left=0
    max_len=0
    count=0
    for right in range(len(nums)):
        if nums[right]==0:
            count+=1
        while count>1:
            if nums[left]==0:
                count-=1
            left+=1
        max_len=max(max_len,right-left+1)

    return max_len-1
nums = [1,1,0,1]
print(longestSubarray(nums))


1004. Max Consecutive Ones III


from typing import List
def longestSubarray(nums: List[int], k: int) -> int:
    left=0
    max_len=0
    count=0
    for right in range(len(nums)):
        if nums[right]==0:
            count+=1
        while count>k:
            if nums[left]==0:
                count-=1
            left+=1
        max_len=max(max_len,right-left+1)

    return max_len
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(longestSubarray(nums,k))

"930:Binary Subarrays With Sum"
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


"1358. Number of Substrings Containing All Three Characters"

from typing import List
def numberOfSubstrings(s: str) -> int:
    last_seen = {'a': 0, 'b': 0, 'c': 0}
    ans = 0
    for i, char in enumerate(s):
        last_seen[char] = i + 1
        ans += min(last_seen['a'], last_seen['b'], last_seen['c'])
    return ans
s = "abcabc"
print(numberOfSubstrings(s))
'''