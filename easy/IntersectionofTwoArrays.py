class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1).intersection(set(nums2)))

s = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(s.intersection(nums1, nums2))