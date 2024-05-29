"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        prev = [1]
        for _ in range(1, rowIndex + 1):
            modified_prev = [0] + prev + [0]
            row = []
            for j in range(len(prev) + 1):
                row.append(modified_prev[j + 1] + modified_prev[j])
            prev = row
            res.append(row)

        return res[-1]


class Solution2:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(1, rowIndex + 1):
            next_element = row[i - 1] * (rowIndex - i + 1) // i
            row.append(next_element)
        return row


s = Solution()
print(s.getRow(3))
assert s.getRow(3) == [1,3,3,1]
print("passed")
