class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        x = []
        for i in nums:
            x.append(i**2)
        return sorted(x)        