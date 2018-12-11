class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = length - 1
        while nums[i] <= nums[i - 1] and i > 0:
            i -= 1
        print(i)
        j = length - 1
        if i > 0:
            while nums[j] <= nums[i -1] and j >= i:
                j -= 1
            print(j)
            temp = nums[i - 1]
            nums[i - 1] = nums[j]
            nums[j] = temp
            print(nums[i:])
            nums[i:].reverse()
            for k in range(i, (length+i)//2):
                temp = nums[k]
                nums[k] = nums[length-1+i-k] 
                nums[length-1+i-k] = temp
        elif i == 0:
            nums.reverse()
s = Solution()
nums = [5, 1, 1]
s.nextPermutation(nums)
print(nums)