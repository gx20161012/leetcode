class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        length = len(nums)
        dict1 = dict()
        for i in range(length):
            if nums[i] not in dict1.keys():
                dict1[nums[i]] = i
            else:
                if i - dict1[nums[i]] < k+1:
                    return True
                else:
                    dict1[nums[i]] = i
        return False
s = Solution()
nums = [1, 0, 1, 1]
print(s.containsNearbyDuplicate(nums, 1))

