class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        list_str = str.split(" ")
        list_pattern = list(pattern)
        length1 = len(list_str)
        length2 = len(list_pattern)
        if length1 != length2:
            return False
        dict1 = dict()
        for i in range(length1):
            if list_pattern[i] not in dict1.keys() and list_str[i] not in dict1.values():
                dict1[list_pattern[i]] = list_str[i]
            elif list_pattern[i] not in dict1.keys() and list_str[i] in dict1.values():
                return False
            elif list_pattern[i] in dict1.keys():
                if dict1[list_pattern[i]] != list_str[i]:
                    return False 
        return True


s = Solution()
pattern = "abca"
str = "dog cat pig dog"
print(s.wordPattern(pattern, str))