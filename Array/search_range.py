# Given a sorted array of integers, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].


class Solution(object):

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = self.searchFirst(nums, target)
        end = self.searchLast(nums, target)

        return [start, end]

    def searchFirst(self, nums, target):
        if nums is None or len(nums) == 0:
            return -1

        start = 0
        end = len(nums) - 1
        while(start <= end):
            mid = start + (end - start) / 2
            n = nums[mid]
            if n == target:
                if mid > 0 and nums[mid - 1] != target or mid == 0:
                    return mid
                else:
                    end = mid - 1
            elif n > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def searchLast(self, nums, target):
        if nums is None or len(nums) == 0:
            return -1

        start = 0
        end = len(nums) - 1
        while(start <= end):
            mid = start + (end - start) / 2
            n = nums[mid]
            if n == target:
                if mid < len(nums) - 1 and nums[mid + 1] != target or mid == len(nums) - 1:
                    return mid
                else:
                    start = mid + 1
            elif n > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
