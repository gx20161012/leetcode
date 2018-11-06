class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        count = 1
        temp = chars[0]
        i = 1
        while i < len(chars):
            if chars[i] == temp:
                count += 1
                temp = chars[i]
                del chars[i]
            else:
                if count == 1:
                    temp = chars[i]
                    count = 1
                    i += 1
                else:
                    for j in range(len(str(count))):
                        chars.insert(i, str(count)[j])
                        i += 1
                    temp = chars[i]
                    count = 1
                    i += 1
        if count == 1:
            return len(chars)
        else:
            for k in range(len(str(count))):
                chars.append(str(count)[k])
            return len(chars)
s = Solution()
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(s.compress(chars))
print(chars)
            