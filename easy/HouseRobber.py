class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 2:
            return max(nums[0], nums[1])
        elif length == 1:
            return nums[0]
        elif length == 0:
            return 0
        cur_max = list()
        cur_max.append(nums[0])
        temp = max(nums[0], nums[1])
        cur_max.append(temp)
        for i in range(2, length, 1):
            t = cur_max[0]
            cur_max[0] = cur_max[1]
            cur_max[1] = max(cur_max[0], t + nums[i])
        return cur_max[1]

s = Solution()
nums = [2,1,1,2]
print(s.rob(nums))