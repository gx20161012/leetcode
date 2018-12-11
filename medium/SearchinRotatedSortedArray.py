class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return -1
        if length == 1 and nums[0] == target:
            return 0
        elif length == 1 and nums[0] != target:
            return -1
        low, high = 0, length - 1
        while low <= high:
            middle = (low + high) // 2
            if target == nums[middle]:
                return middle
            if nums[low] > nums[middle]:
                if nums[middle] <= target <= nums[high]:
                    low = middle + 1
                else:
                    high = middle - 1
            else:
                if nums[low] <= target <= nums[middle]:
                    high = middle - 1
                else:
                    low = middle + 1
        return -1

s = Solution()
nums = [3,1]
print(s.search(nums, 1))
