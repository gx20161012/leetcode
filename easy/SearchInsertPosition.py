class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            length = len(nums)
            for i in range(length):
                if nums[i] < target:
                    continue
                else:
                    nums.insert(i, target)
                    return i
            nums.append(target)
            return len(nums) - 1
s = Solution()
nums = [1,3,5,6]
val = 1
print(s.searchInsert(nums, val))
print(nums)
