class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        list_list = list()
        nums = sorted(nums)
        if len(nums) == 0:
            return list_list
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            k = i + 1
            j = len(nums) - 1
            while k < j:
                if nums[k] + nums[j] == target:
                    list_list.append([nums[i], nums[k], nums[j]])
                    while k < j and nums[k] == nums[k+1]:
                        k += 1
                    while k < j and nums[j] == nums[j-1]:
                        j -= 1
                    k += 1
                    j -= 1
                elif nums[k] + nums[j] < target:
                    k += 1
                else:
                    j -= 1
        return list_list
s = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(s.threeSum(nums))