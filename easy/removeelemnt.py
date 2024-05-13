"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
    Return k.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = 0
        start, last = 0, len(nums) - 1
        while start <= last:
            if nums[start] == val:
                nums[start], nums[last] = nums[last], nums[last]
                last -= 1
            else:
                ans += 1
                start += 1
        return ans

s = Solution()
n = [3,2,2,3]
assert s.removeElement(n, 3) == 2 and n[0:2] == [2, 2]
n = [0,1,2,2,3,0,4,2]
assert s.removeElement(n, 2) == 5 and n[0:5] == [0, 1, 4, 0, 3]
print("passed")
