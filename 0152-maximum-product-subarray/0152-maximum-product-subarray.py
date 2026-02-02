class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minprod = nums[0]
        maxprod = nums[0]
        res = nums[0]

        for i in nums[1:]:

            if i < 0:
               minprod,maxprod = maxprod,minprod

            maxprod = max(i, maxprod * i)
            minprod = min(i, minprod * i)
            res = max(res,maxprod)
        return res
        