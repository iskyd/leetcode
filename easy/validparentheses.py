"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""

M = {
    '(': ')',
    '[': ']',
    '{': '}',
}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                l = stack.pop()
                if M[l] != c:
                    return False
        return True if len(stack) == 0 else False

s = Solution()
assert s.isValid("()") == True
assert s.isValid("()[]{}") == True
assert s.isValid("(]") == False
assert s.isValid("(") == False
assert s.isValid(")") == False
print("passed")
