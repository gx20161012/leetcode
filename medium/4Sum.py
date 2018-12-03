class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        list_list = list()
        nums = sorted(nums)
        length = len(nums)
        for i in range(0, length-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, length-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = length - 1
                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum == target:
                        list_num = [nums[i], nums[j], nums[left], nums[right]]
                        list_list.append(list_num)
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif sum < target:
                        left += 1
                    else:
                        right -= 1
        return list_list 
s = Solution()
nums = [1, 0, -1, 0, -2, 2]
print(s.fourSum(nums, 0))