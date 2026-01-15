class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        res = 0

        for i in range (len(nums)):

            if nums[i] < target:
                res += 1

        return res