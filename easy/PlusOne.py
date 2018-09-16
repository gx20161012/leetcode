#Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#The digits are stored such that the most significant digit is at the head of the list, 
# and each element in the array contain a single digit.
#You may assume the integer does not contain any leading zero, except the number 0 itself.
class Solution:
    def plusOne(self, s,digits):
        """
        :type s: int
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        a = digits[length-1] + s
        if a < 10:
            digits[length-1] += s
            return digits
        else:
            digits[length-1] = a - 10
            for i in range(length):
                if i == length-2:
                    if digits[length-i-2] + 1 >= 10:
                        digits[length-i-2] = digits[length-i-2] + 1 - 10
                        digits.insert(0,1)
                        break
                    else:
                        digits[length-2-i] += 1
                        break
                if digits[length-i-2] + 1 >= 10:
                    digits[length-i-2] = digits[length-i-2] + 1 - 10
                else:
                    digits[length-2-i] += 1
                    break
        return digits
s = Solution()
digits = [9,9,8]
print(s.plusOne(7, digits))