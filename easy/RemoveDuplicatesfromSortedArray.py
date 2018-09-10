#Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) != 0:
            count = 1
            temp = nums[0]
            for i in range(1,len(nums),1):
                if temp != nums[i]:
                    temp = nums[i]
                    count = count + 1
                else:
                    nums[i]='A'
            num = nums.count('A')
            for j in range(num):
                nums.remove('A')
            return count
        else:
            return 0

s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(nums))
print(nums)
