class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(numbers)
        a = 0
        b = length - 1
        while numbers[a] + numbers[b] != target:
            if numbers[a] + numbers[b] > target:
                b -= 1
                continue
            elif numbers[a] + numbers[b] < target:
                a += 1
        return [a+1, b+1] 



s = Solution()
numbers = [0,1,0,11]
target = 0
print(s.twoSum(numbers, target))