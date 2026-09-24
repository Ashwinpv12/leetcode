# Smallest Index With Digit Sum Equal to Index
class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if sum(int(digit) for digit in str(nums[i])) == i:
                return i
        return -1