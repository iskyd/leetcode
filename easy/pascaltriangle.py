"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        res = [[1]]
        prev = [1]
        for _ in range(1, numRows):
            modified_prev = [0] + prev + [0]
            row = []
            for j in range(len(prev) + 1):
                row.append(modified_prev[j + 1] + modified_prev[j])
            prev = row
            res.append(row)

        return res


s = Solution()
assert s.generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
assert s.generate(1) == [[1]]
print("passed")
