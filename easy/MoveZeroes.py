class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for i in range(length):
            if nums[i] == 0:
                for j in range(i+1, length, 1):
                    if nums[j] != 0:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
                        break
                    else:
                        continue
            else:
                continue
s = Solution()
nums = [0,0,0,3,12]
s.moveZeroes(nums)
print(nums)