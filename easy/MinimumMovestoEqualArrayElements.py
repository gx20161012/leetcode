class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_nums = min(nums)
        return sum(nums) - len(nums) * min_nums
s = Solution()
nums = [1, 2, 4]
print(s.minMoves(nums))