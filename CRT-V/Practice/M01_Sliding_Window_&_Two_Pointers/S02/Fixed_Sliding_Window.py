'''
leetcode 643:-

from typing import List
def findMaxAverage(nums: List[int], k: int) -> float:
    max_sum=float("-inf")
    n=len(nums)
    for i in range(n-k+1):
        sub_sum=0
        for j in range(i,k+i):
            sub_sum+=nums[j]
        max_sum=max(max_sum,sub_sum)
    return max_sum/k 
nums=[1,12,-5,-6,50,3]
k=4
print(findMaxAverage(nums,k))

from typing import List
def findMaxAverage_Optimal(nums: List[int], k: int) -> float:
    win_sum=sum(nums[:k])
    max_sum=win_sum
    n=len(nums)
    for i in range(0,n-k):
        win_sum=win_sum-nums[i]+nums[k+i]
        max_sum=max(win_sum,max_sum)
    return max_sum/k 
nums=[1,12,-5,-6,50,3]
k=4
print(findMaxAverage_Optimal(nums,k))


leetcode 1343:-

from typing import List
def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
    count=0
    n=len(arr)
    win_sum=sum(arr[:k])
    if (win_sum/k)>=threshold:
        count+=1
    for i in range(0,n-k):
        win_sum=win_sum-arr[i]+arr[k+i]
        if (win_sum/k)>=threshold:
            count+=1
    return count
arr = [2,2,2,2,5,5,5,8] 
k = 3
threshold = 4
print(numOfSubarrays(arr,k,threshold))


leetcode 1456:-

from typing import List
def maxVowels(s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    current_vowels = sum(1 for i in range(k) if s[i] in vowels)
    max_vowels = current_vowels
    for i in range(k, len(s)):
        if s[i] in vowels:
            current_vowels += 1
        if s[i - k] in vowels:
            current_vowels -= 1
            
        if current_vowels > max_vowels:
            max_vowels = current_vowels
                
        if max_vowels == k:
            return k
                
    return max_vowels
s = "abciiidef"
k = 3
print(maxVowels(s,k))
'''