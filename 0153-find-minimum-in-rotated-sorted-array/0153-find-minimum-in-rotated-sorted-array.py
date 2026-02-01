class Solution:
    def findMin(self, nums: List[int]) -> int:
        minval  = float('inf')
        for i in nums:
            minval = min(minval,i)
        return minval
        