class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        list_res = [""]
        dict_num = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], 
                    '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], 
                    '8':['t','u','v'], '9':['w','x','y','z']}
        for char in digits:
            list_t = list()
            string = dict_num[char]
            for i in range(len(string)):
                for s in list_res:
                    list_t.append(s+string[i])
                print(list_t)
            list_res = list_t
        return list_res
s = Solution()
digits = '234'
print(s.letterCombinations(digits))
