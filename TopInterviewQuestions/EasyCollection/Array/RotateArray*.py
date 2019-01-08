class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        '''
        if nums:
            length = len(nums)
            k = k % length
            while k > 0:
                temp = nums[length-1]
                j = length - 1
                while j > 0:
                    nums[j] = nums[j-1]
                    j -= 1
                nums[0] = temp
                k -= 1
        '''
        if nums:
            length = len(nums)
            k = k % length
            self.reverse(nums, 0, length-k-1)
            self.reverse(nums, length-k, length-1)
            self.reverse(nums, 0, length-1)
    def reverse(self, nums, a, b):
        while a < b:
            temp = nums[a]
            nums[a] = nums[b]
            nums[b] = temp
            a += 1
            b -= 1
nums = [1,2,3,4,5,6,7]
k = 3
s = Solution()
s.rotate(nums, k)
print(nums)
            
                
                    