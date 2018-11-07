class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        length = len(points)
        count = 0
        for i in range(length):
            dict_dis = dict()
            for j in range(length):
                if points[i] == points[j]:
                    continue
                distance = self.getDistance(points[i], points[j])
                if distance not in dict_dis.keys():
                    dict_dis[distance] = 1
                else:
                    dict_dis[distance] += 1
            for key in dict_dis.keys():
                count += dict_dis[key] * (dict_dis[key] - 1)
        return count
    def getDistance(self, i, j):
        """
        :type i, j: List[int]
        :rtype: int
        """
        return (i[0]-j[0]) ** 2 + (i[1]-j[1]) ** 2
s = Solution()
points = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]
print(s.numberOfBoomerangs(points))