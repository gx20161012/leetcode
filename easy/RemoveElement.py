class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = nums.count(val)
        for i in range(count):
            nums.remove(val)
        return len(nums)
s = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
print(s.removeElement(nums, val))
print(nums)