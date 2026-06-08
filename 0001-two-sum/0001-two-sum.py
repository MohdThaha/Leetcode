class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mp = {}

        for ind, num in enumerate(nums):
            rem = target - num
            if rem in mp:
                return [mp[rem],ind]
            mp[num]=ind
