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
nums = [4,1,2,1,2]
s = Solution()
print(s.singleNumber(nums))