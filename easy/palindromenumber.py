"""
Given an integer x, return true if x is a palindrome , and false otherwise.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

    
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        xs = str(x)
        i, j = 0, len(xs) - 1
        while(i < j):
            if xs[i] != xs[j]:
                return False
            i += 1
            j -= 1
        return True


s = Solution2()
assert s.isPalindrome(121) == True
assert s.isPalindrome(-121) == False
print("passed")
