class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        self.backtrack(result, [], candidates, target, 0)
        return result

    def backtrack(self, result, temp, nums, remain, start):
        if remain <  0:
            return False
        elif remain == 0:
            result.append(temp.copy())
            return False
        else:
            for i in range(start, len(nums), 1):
                temp.append(nums[i])
                flag = self.backtrack(result, temp, nums, remain-nums[i], i)
                temp.remove(nums[i])
                if flag == False:
                    break
                
            return True
s = Solution()
print(s.combinationSum([8,7,4,3], 11))