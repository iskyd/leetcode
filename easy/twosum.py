"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]

        raise ValueError

    
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        n = len(nums)

        for i in range(n):
            s = target - nums[i]
            if s in m:
                return [m[s], i]
            m[nums[i]] = i
        

        raise ValueError

    

s = Solution2()
assert s.twoSum([2,7,11,15], 9) == [0, 1]
assert s.twoSum([3,2,4], 6) == [1, 2]

print("passed")
