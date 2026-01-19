class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        res = []
        nums.sort()
        j = 1
        
        for i in nums:
            while i > j:
                res.append(j)
                j += 1
            if i == j:
                j += 1
        
        while  j != len(nums) + 1:
           res.append(j) 
           j += 1
        
        return res
        