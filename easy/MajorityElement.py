'''
Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.
'''
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        set1 = set()
        for i in range(length):
            if nums[i] in set1:
                continue
            if nums.count(nums[i]) > length / 2:
                return nums[i]
            else:
                set1.add(nums[i])

s = Solution()
nums = [2, 2, 1, 1, 2]
print(s.majorityElement(nums))