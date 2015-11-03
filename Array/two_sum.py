# Given an array of integers, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
#
# You may assume that each input would have exactly one solution.
#
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i in range(len(nums)):
            if target - nums[i] in d:
                index1 = i + 1
                index2 = d[target-nums[i]] + 1
                return [index1 if index1 < index2 else index2, index2 if index2 > index1 else index1]
            d[nums[i]] = i
        return []

if __name__ == '__main__':
    print Solution().twoSum([3,2,4], 6)
