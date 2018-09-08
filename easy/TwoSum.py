#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in nums:
            if target-i in nums and i != target-i:
                result.append(nums.index(i))
                result.append(nums.index(target-i))
                break
            elif target-i in nums and i == target-i and nums.count(i) >= 2:
                index = nums.index(i)
                result.append(index)
                nums1 = nums
                nums1[index] = 'a'
                result.append(nums1.index(i))
                break
            else:
                continue
        return result
nums = [3,3]
target = 6
s = Solution()
print(s.twoSum(nums, target))
        