'''
3. Longest Substring Without Repeating Characters

from typing import List
def lengthOfLongestSubstring(s: str) -> int:
    left=0
    ans=0
    char_set=set()
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left+=1
        char_set.add(s[right])
        ans=max(ans,right-left+1)
    return ans
s = "abcabcbb"
print(lengthOfLongestSubstring(s))


424. Longest Repeating Character Replacement
'''
from typing import List
def characterReplacement(s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        max_length = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
s = "AABABBA"
k = 1
print(characterReplacement(s,k))