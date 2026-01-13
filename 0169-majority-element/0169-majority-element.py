class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = 0
        variable = None

        for i in nums:
            if count == 0:
                variable = i
            
            if i == variable:
                count += 1
            else:
                count -= 1
        
        return variable