class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [-1,-1]
        if not nums:
            return result
        length = len(nums)
        if length == 1 and target == nums[0]:
            return [0, 0]
        low, high = 0, length-1
        while low < high:
            middle = (low + high) // 2
            if nums[middle] < target:
                low = middle + 1
            elif nums[middle] > target:
                high = middle - 1
            else:
                low = middle
                high = middle
                while low-1 >= 0 and nums[low-1] == target:
                        low -= 1
                while high+1 < length and nums[high+1] == target:
                        high += 1
                break
        if nums[low] == target:
            result[0] = low
            result[1] = high
        return result

s = Solution()
nums = [5, 7, 7, 8, 8, 10]
print(s.searchRange(nums, 8))              
