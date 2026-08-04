
'''leetcode:- 1763

from typing import List
def longestNiceSubstring(s: str) -> str:
    if len(s)<2:
        return ""
    uniq=set(s)
    for i , ch in enumerate(s):
        if ch.lower() in uniq and ch.upper() in uniq:
            continue
        sub1=longestNiceSubstring(s[:i])
        sub2=longestNiceSubstring(s[i + 1:])
        return sub1 if len(sub1) >= len(sub2) else sub2
    return s
s = "YazaAay"
print(longestNiceSubstring(s))

'''