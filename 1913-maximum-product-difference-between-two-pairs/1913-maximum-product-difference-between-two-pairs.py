class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()

        p11 = nums[0]
        p12 = nums[1]
        p21 = nums[-1]
        p22 = nums[-2]

        result = ( ( p22 * p21 ) - ( p12 * p11) )

        return result