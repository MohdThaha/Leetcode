class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash = {}

        for i,j in enumerate(nums):
            rem  = target - j
            if rem in hash:
                return [hash[rem],i]
            hash[j] = i

        