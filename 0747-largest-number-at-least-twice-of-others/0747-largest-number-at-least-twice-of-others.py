class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        max1 = -1
        max2 = -1
        idx = -1

        for i,num in enumerate(nums):
            if num > max1:
                max2 = max1 
                max1 = num
                idx= i
            elif num > max2:
                max2 = num

        return idx if max1 >= max2 * 2 else -1
