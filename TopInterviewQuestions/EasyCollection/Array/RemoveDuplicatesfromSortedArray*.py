class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            '''
            '''
            length = len(nums)
            temp = nums[0]
            for i in range(1, length):
                if nums[i] == temp:
                    nums[i] = "dup"
                else:
                    temp = nums[i]
            while "dup" in nums: 
                nums.remove("dup")
        return len(nums)
nums = [1, 1, 2]
s = Solution()
print(s.removeDuplicates(nums))
print(nums)