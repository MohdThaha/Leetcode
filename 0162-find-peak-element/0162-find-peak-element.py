class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        idx = 0
        maxval = float('-inf')

        for i,j in enumerate(nums):
            if j > maxval:
                maxval = j
                idx = i
        return idx