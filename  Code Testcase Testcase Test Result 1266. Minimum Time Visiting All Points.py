class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        x, y = points[0]
        for i in range(1, len(points)):
            x1, y1 = points[i]
            res += max(abs(x-x1), abs(y-y1))
            x, y = x1, y1
        return res