class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        list_disappear = list()
        for i in range(length):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        for i in range(length):
            if nums[i] > 0:
                list_disappear.append(i+1)
        return list_disappear
s = Solution()
nums = [4,3,2,7,8,2,3,1]
print(s.findDisappearedNumbers(nums))
