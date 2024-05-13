"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


# Attempt to avoid using find
# Slower then find (exepected, otherwise I would be the one who wrote the find implementation).
class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        start = 0
        print(len(haystack) - len(needle) + 1)
        while start < len(haystack) - len(needle) + 1:
            res = True
            for i in range(len(needle)):
                if needle[i] != haystack[start+i]:
                    res = False
                    break
            if res is True:
                return start

            start += 1
            
        return -1
    
s = Solution2()
assert s.strStr("sadbutsad", "sad") == 0
assert s.strStr("leetcode", "leeto") == -1
print("passed")
