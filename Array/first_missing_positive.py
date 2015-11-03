# Given an unsorted integer array, find the first missing positive integer.
#
# For example,
# Given[1, 2, 0] return 3,
#[3, 4, -1, 1] return 2.
#
# Your algorithm should run in O(n) time and uses constant space.

class Solution(object):

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 1
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] > 0 and nums[i] != i + 1 and nums[i] < n + 1 and nums[nums[i] - 1] != nums[i]:
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp

            else:
                i += 1
        for i in range(0, n):
            if nums[i] != i + 1:
                return i + 1

        return n+1

if __name__ == '__main__':
    print Solution().firstMissingPositive([1])
