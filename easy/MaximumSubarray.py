# Given an integer array nums, 
# find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = g = -1000000000
        for n in nums:
            l = max(n,l+n)
            g = max(l,g)
        return g

s = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(nums))