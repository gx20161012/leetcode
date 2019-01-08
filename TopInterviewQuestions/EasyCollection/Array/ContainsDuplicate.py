class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums:
            length = len(nums)
            set1 = set()
            for i in range(length):
                set1.add(nums[i])
                if len(set1) != i+1:
                    return True
            return False
        return False
nums = [1,2,3,4]
s = Solution()
print(s.containsDuplicate(nums))