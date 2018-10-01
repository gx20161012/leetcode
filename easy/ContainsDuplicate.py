class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        set1 = set()
        for i in range(length):
            set1.add(nums[i])
            if len(set1) != i+1:
                return True
        return False

s = Solution()
nums = [1,1,1,3,3,4,3,2,4,2]
print(s.containsDuplicate(nums))
