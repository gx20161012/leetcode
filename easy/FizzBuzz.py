class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list1 = list()
        for i in range(1, n+1, 1):
            if i % 3 != 0 and i % 5 != 0:
                list1.append(str(i))
            elif i % 3 == 0 and i % 5 != 0:
                list1.append("Fizz")
            elif i % 3 != 0 and i % 5 == 0:
                list1.append("Buzz")
            else:
                list1.append("FizzBuzz")
        return list1

s = Solution()
print(s.fizzBuzz(15))