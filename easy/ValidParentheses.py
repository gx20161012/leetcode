#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Note that an empty string is also considered valid.
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list1 = list(s)
        list2 = list()
        left = ['(', '[', '{']
        right = [')', ']', '}']
        for char in list1:
            if char in left:
                list2.append(char)
            elif char in right:
                if len(list2) != 0:
                    char1 = list2.pop()
                    if (char == ')' and char1 == '(') or (char == '}' and char1 == '{') or (char == ']' and char1 == '['):
                        continue
                    else:
                        return False
                else:
                    return False
        if len(list2) == 0:
            return True
        else:
            return False




s = Solution()
print(s.isValid("]"))