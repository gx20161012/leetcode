class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # I:1 V:5 X:10 L:50 C:100 D:500 M:1000
        list1 = []
        for char in s:
            if char == 'I':
                list1.append(1)
            elif char == 'V':
                list1.append(5)
            elif char == 'X':
                list1.append(10)
            elif char == 'L':
                list1.append(50)
            elif char == 'C':
                list1.append(100)
            elif char == 'D':
                list1.append(500)
            else:
                list1.append(1000)
        sum = 0
        for i in range(len(list1)-1):
            if list1[i] >=list1[i+1]:
                sum = sum  + list1[i]
            else:
                sum = sum -list1[i]
        return sum + list1[len(list1)-1]

s = Solution()
print(s.romanToInt("III"))