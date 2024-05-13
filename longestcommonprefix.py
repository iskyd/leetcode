"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = min(map(len, strs))
        ans = ""
        for i in range(l):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != c:
                    return ans
            ans += c
            
        return ans


# Slower but shorter. Not sure about readability
class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = min(map(len, strs))
        ans = ""
        for i in range(l):
            if len(set([s[i] for s in strs])) != 1:
                return ans
            ans += strs[0][i]
            
        return ans
    
    
s = Solution2()
assert s.longestCommonPrefix(["flower","flow","flight"]) == "fl"
assert s.longestCommonPrefix(["dog","racecar","car"]) == ""
print("passed")
