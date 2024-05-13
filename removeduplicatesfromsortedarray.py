"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
    Return k.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.
"""


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = set(nums)
        nums[0:len(x)] = sorted(list(x))
        return len(x)


s = Solution()
n = [1,1,2]
assert s.removeDuplicates(n) == 2 and n[0:2] == [1, 2]

n = [-1,0,0,0,0,3,3]
assert s.removeDuplicates(n) == 3 and n[0:3] == [-1, 0, 3]
print("passed")
