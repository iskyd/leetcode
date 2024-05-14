"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

import functools


# First approach with memoization
class Solution:
    def climbStairs(self, n: int) -> int:
        @functools.cache
        def inner(n: int, current: int, s: int):
            if current + s > n:
                return 0
            elif current + s == n:
                return 1
            else:
                return inner(n, current + s, 1) + inner(n, current + s, 2)

        return inner(n, 0, 1) + inner(n, 0, 2)


class Solution2:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n - 1) +  self.climbStairs(n - 2)


class Solution3:
    def climbStairs(self, n: int) -> int:
        @functools.cache
        def inner(n: int) -> int:
            if n == 0 or n == 1:
                return 1
            return inner(n - 1) +  inner(n - 2)

        return inner(n)

    
s = Solution3()
assert s.climbStairs(2) == 2
assert s.climbStairs(3) == 3
assert s.climbStairs(38) == 63245986
print("succeded")
