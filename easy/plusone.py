"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""


from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = list()

        remainder = 0
        if digits[-1] + 1 > 9:
            res.append(0)
            remainder = 1
        else:
            res.append(digits[-1] + 1)

        cur = len(digits) - 2
        while cur >= 0 or remainder == 1:
            n = digits[cur] if cur >= 0 else 0
            if n + remainder > 9:
                res.append(0)
                remainder = 1
            else:
                res.append(n + remainder)
                remainder = 0
            cur -= 1

        return res[::-1]


s = Solution()
assert s.plusOne([1, 2, 3]) == [1, 2, 4]
assert s.plusOne([4,3,2,1]) == [4,3,2,2]
assert s.plusOne([9]) == [1,0]
print("succeded")
