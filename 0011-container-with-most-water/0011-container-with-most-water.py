class Solution:
    def maxArea(self, height: List[int]) -> int:

        x = 0
        y = len(height)-1
        ans = 0

        while (x<y):
            l = min(height[x],height[y])
            b = y - x
            ans =max( ans, l*b )

            if height[x] > height[y]:
                y-=1
            else:
                x+=1
        return ans