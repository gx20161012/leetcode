"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
"""
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        res = 0
        for i in range(length):
            res ^= nums[i]
        return res

s = Solution()
nums = [1,2,3,2,3,1,4]
num = s.singleNumber(nums)
print(num)