class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()

        x=1
        for i in nums:
            if i <= 0:
                continue
            elif x == i:
                x+=1
            elif i > x :
                return x
        
        return x