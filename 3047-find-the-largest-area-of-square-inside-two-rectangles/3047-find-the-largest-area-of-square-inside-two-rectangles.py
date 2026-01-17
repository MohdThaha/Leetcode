class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        res = 0

        for i in range(n):
            for j in range(i+1,n):

                left = max(bottomLeft[i][0], bottomLeft[j][0])
                bottom = max(bottomLeft[i][1], bottomLeft[j][1])
                right = min(topRight[i][0], topRight[j][0])
                top = min(topRight[i][1], topRight[j][1])
        
                if left < right and bottom < top:
                    side = min(right - left, top - bottom)
                    res = max(res, side * side)

        return res