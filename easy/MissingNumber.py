class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if 0 not in nums:
            return 0
        sum = 0
        for i in range(length):
            sum += nums[i]
        sum1 = max(nums) * (max(nums)+1) / 2
        if sum <  sum1:
            return int( sum1- sum)
        elif sum == sum1:
            return max(nums)+1

s = Solution()
nums = [1]
print(s.missingNumber(nums))