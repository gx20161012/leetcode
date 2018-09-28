'''
Given an array, rotate the array to the right by k steps, where k is non-negative
'''
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        remainder = k % length
        split = length - remainder
        self.reverse(nums, 0, split-1)
        self.reverse(nums, split, length-1)
        self.reverse(nums, 0, length-1)
    
    def reverse(self, nums, a, b):
        while a < b:
            temp = nums[a]
            nums[a] = nums[b]
            nums[b] = temp

            a += 1
            b -= 1

s = Solution()
nums = [1,2,3,4,5,6,7]
s.rotate(nums, 7)
print(nums)
