class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:

        start = nums[0]
        count = 1
        res = 1

        for i in range(1,len(nums)):
            if nums[i] > start:
                start = nums[i]
                count+=1
            else:
                res = max(res,count)
                count = 1
                start = nums[i]
            res = max(res,count)
        return res