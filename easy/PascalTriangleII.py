class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        list1 = [[1], [1, 1]]
        for i in range(2, rowIndex+1):
            list2 = list()
            for index in range(len(list1[i-1])):
                if index == 0:
                    list2.append(1)
                    continue
                list2.append(list1[i-1][index-1]+ list1[i-1][index])
            list2.append(1)
            list1.append(list2)
        return list1[rowIndex]


s = Solution()
print(s.getRow(5))
