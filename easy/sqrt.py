"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x
        while start <= end:
            mid = (start + end) // 2
            p = mid * mid
            if p == x:
                return mid
            elif p > x:
                end = mid - 1
            else:
                start = mid + 1

        return start - 1
            


s = Solution()
assert s.mySqrt(4) == 2
assert s.mySqrt(8) == 2
assert s.mySqrt(9) == 3
assert s.mySqrt(10) == 3
assert s.mySqrt(15) == 3

print("succeded")
