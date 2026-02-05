class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        start = nums[0]
        count = 1
        res = 1

        for i in range(1, len(nums)):
            if nums[i] > start:
                count += 1
            else:
                count = 1
            start = nums[i]
            res = max(res, count)

        return res
