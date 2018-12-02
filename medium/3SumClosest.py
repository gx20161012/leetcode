class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest = nums[0] + nums[1] + nums[2]
        diff = abs(closest-target)
        nums = sorted(nums)
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                newdiff = abs(sum - target)
                if diff > newdiff:
                    diff = newdiff
                    closest = sum
                if sum < target:
                    left += 1
                else:
                    right -= 1
        return closest
s = Solution()
nums = [-1, 2, 1, -4]
print(s.threeSumClosest(nums, 1))