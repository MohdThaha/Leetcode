class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        current_sum = 0
        result =  float('inf') 

        for r in range(len(nums)):
            current_sum+=nums[r]

            while current_sum >= target:
                result = min(result,r-l+1)
                current_sum-=nums[l]
                l+=1
        return 0 if result == float('inf') else result 