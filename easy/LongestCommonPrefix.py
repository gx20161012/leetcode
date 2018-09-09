#Write a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str] 
        :rtype: str
        """
        set1 = set()
        list1 = list()
        i = 0
        while True:
            for string in strs:
                if(i == len(string) or string == ""):
                    str2 = ""
                    for i in list1:
                        str2 = str2 + i
                    return str2
                set1.add(string[i])
            if len(set1) == 1:
                list1.append(set1.pop())
                i = i + 1
            else:
                list1.append("")
                break
        str1 = ""
        for i in list1:
            str1 = str1 + i
        return str1
s = Solution()
strs = ["acbb","a",]
print(s.longestCommonPrefix(strs))   

