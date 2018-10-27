class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_vowel = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        list_s = list(s)
        left = 0
        right = len(list_s) - 1
        while left < right:
            if list_s[left] in list_vowel and list_s[right] in list_vowel:
                temp = list_s[left]
                list_s[left] = list_s[right]
                list_s[right] = temp
                left += 1
                right -= 1
            elif list_s[left] not in list_vowel:
                left += 1
            elif list_s[right] not in list_vowel:
                right -= 1
        string = ''
        for s in list_s:
            string += s
        return string
s = Solution()
print(s.reverseVowels('aA'))
