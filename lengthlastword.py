"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])


s = Solution()
assert s.lengthOfLastWord("Hello World") == 5
assert s.lengthOfLastWord("   fly me   to   the moon  ") == 4
print("passed")
