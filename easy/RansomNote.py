class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        length1 = len(ransomNote)
        length2 = len(magazine)
        if length1 > length2:
            return False
        dict1 = dict()
        for i in range(length2):
            if magazine[i] not in dict1.keys():
                dict1[magazine[i]] = 1
            else:
                dict1[magazine[i]] += 1
        for i in range(length1):
            if ransomNote[i] not in dict1.keys() or dict1[ransomNote[i]] < 1:
                return False
            elif ransomNote[i] in dict1.keys() and dict1[ransomNote[i]] > 0:
                dict1[ransomNote[i]] -= 1
        return True
s = Solution()
ransomNote = "fihjjjjei"

magazine = "hjibagacbhadfaefdjaeaebgi" 
print(s.canConstruct(ransomNote, magazine))